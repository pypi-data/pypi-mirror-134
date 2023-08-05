import aioredis
import json

from unittest import IsolatedAsyncioTestCase

from eyja.main import Eyja

from eyja_email.operators import EmailOperator


class EmailTest(IsolatedAsyncioTestCase):
    redis_url = 'redis://localhost:30002/4'
    config = '''
        storages:
            rethinkdb:
                port: 30001
                password: 123456
                db:
                -   test_db
        email:
            templates: tests/templates
            smtp:
                host: localhost
                port: 30003
    '''

    async def test_send_email(self):
        await Eyja.reset()
        await Eyja.init(
            config=self.config,
            plugins=['eyja_rethinkdb']
        )

        email = await EmailOperator.create(
            subject='Test email',
            sender='test1@test.com',
            sender_name='Test Sender',
            recipient='test2@test.com',
            template='test.j2',
            message_data={
                'test_email': 'test2@test.com',
                'test_data': 'cool'
            }
        )

        await EmailOperator.send(email)

        redis_connection = aioredis.from_url(self.redis_url)
        async with redis_connection.client() as conn:
            redis_data = await conn.get(email.object_id)

        message = json.loads(redis_data.decode())

        self.assertEqual(message['message']['subject'], email.subject)
        self.assertEqual(message['message']['body']['text'], email.subject)
        self.assertEqual(
            message['message']['body']['html'], 
            '<html>\r\n    <body>\r\n        <p>\r\n            Hello, <b>test2@test.com</b>, cool!\r\n        </p>\r\n    </body>\r\n</html>'
        )
