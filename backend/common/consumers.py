from channels.generic.websocket import AsyncWebsocketConsumer


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        if self.scope["contact_person"]:
            contact_person = self.scope["contact_person"]
            self.group_name = (
                f"restaurant_{contact_person['restaurant_code']}"
                if contact_person["is_restaurant_user"]
                else f"user_{contact_person['user_id']}"
            )

            await self.channel_layer.group_add(self.group_name, self.channel_name)
            await self.accept()
        else:
            await self.close()

    async def disconnect(self, close_code=None):
        if self.group_name is not None:
            await self.channel_layer.group_discard(self.group_name, self.channel_name)
        await self.close()

    async def notify_restaurant(self, event):
        await self.send(text_data=event["message"])

    async def notify_user(self, event):
        await self.send(text_data=event["message"])
