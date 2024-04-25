from backend.common.services import BaseNotificationService


class UserNotificationService(BaseNotificationService):
    def __init__(self, user_id=None, *args, **kwargs):
        super().__init__(group_name=f"user_{user_id}", *args, **kwargs)

    def send_notification(self, **kwargs):
        self.send_to_group({"type": "notify.user", **kwargs})
