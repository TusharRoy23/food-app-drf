from backend.common.services import BaseNotificationService


class RestaurantNotificationService(BaseNotificationService):
    def __init__(self, code=None, *args, **kwargs):
        super().__init__(group_name=f"restaurant_{code}", *args, **kwargs)

    def send_notification(self, **kwargs):
        # TODO: Need a way to check notification confirmation
        self.send_to_group({"type": "notify.restaurant", **kwargs})
