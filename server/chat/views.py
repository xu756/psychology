import json

from channels.exceptions import StopConsumer
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class ChatConsumer(WebsocketConsumer):

    def websocket_connect(self, message):
        # 异步发送消息
        # 把异步发送消息改为同步发送消息
        async_to_sync(self.channel_layer.group_add)(
            "chat", self.channel_name
        )
        self.accept()

    def websocket_receive(self, message):
        async_to_sync(self.channel_layer.group_send)(
            "chat", {
                "type": "send.message",
                "message": message
            }
        )

    def send_message(self, event):
        text = event["message"]["text"]
        print(event)
        self.send(text)     # 给所有人发送消息


def websocket_disconnect(self, message):
    async_to_sync(self.channel_layer.group_discard)(
        "chat", self.channel_name
    )
    # 断开连接
    raise StopConsumer()
