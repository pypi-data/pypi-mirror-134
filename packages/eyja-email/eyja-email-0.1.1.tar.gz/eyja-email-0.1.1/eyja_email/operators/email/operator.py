import aiosmtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from eyja.hubs.config_hub import ConfigHub
from eyja.utils import load_model, render_template

from eyja_email.models import Email

from .statuses import EmailStatuses


class EmailOperator:
    statuses = EmailStatuses

    @classmethod
    async def send(cls, email: Email):
        rendered_template = await render_template(
            template_root=ConfigHub.get('email.templates'),
            template=email.template,
            data=email.message_data
        )

        message = MIMEMultipart('alternative')
        message['Subject'] = email.subject
        message['From'] = f'{email.sender_name} <{email.sender}>'
        message['To'] = email.recipient
        message['Reply-To'] = email.sender
        message['Return-Path'] = email.sender
        message['X-Mailer'] = ConfigHub.get('email.mailer', 'Eyja')
        message['Message-ID'] = f'<{email.object_id}>'

        part_text = MIMEText(email.subject, 'plain')
        part_html = MIMEText(rendered_template, 'html')

        message.attach(part_text)
        message.attach(part_html)

        await aiosmtplib.send(
            message=message,
            hostname=ConfigHub.get('email.smtp.host'),
            port=ConfigHub.get('email.smtp.port'),
            username=ConfigHub.get('email.smtp.user'),
            password=ConfigHub.get('email.smtp.password'),
            use_tls=ConfigHub.get('email.smtp.use_tls'),
        )

    @classmethod
    async def create(cls, **params):
        email_model = load_model('email.model', Email)
        
        params.setdefault('status', cls.statuses.NEW)

        email = email_model(**params)
        await email.save()

        return email
