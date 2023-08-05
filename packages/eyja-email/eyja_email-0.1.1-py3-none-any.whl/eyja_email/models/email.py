from eyja.interfaces.db import BaseStorageModel
from eyja.hubs.config_hub import ConfigHub


class Email(BaseStorageModel):
    _namespace = ConfigHub.get('email.namespace', ':::emails')
    _indexes = [
        'sender',
        'recipient'
    ] + BaseStorageModel._indexes

    subject: str
    sender: str
    sender_name: str
    recipient: str
    template: str
    message_data: dict
    status: str

    async def save(self) -> None:
        if ConfigHub.get('email.save_messages', True):
            await super().save()
