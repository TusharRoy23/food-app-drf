from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


class BaseNotificationService:
    def __init__(self, channel_name=None, group_name=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.channel_layer = get_channel_layer()
        self.channel_name = channel_name
        self.group_name = group_name

    def send_to_group(self, data):
        async_to_sync(self.channel_layer.group_send)(self.group_name, data)  # noqa
