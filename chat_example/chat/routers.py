from swampdragon import route_handler
from swampdragon.route_handler import BaseRouter, ModelRouter

from chat_example.chat.Models import Message
from chat_example.chat.serializers import MessageSerializer


class ChatRouter(BaseRouter):
    route_name = 'chat-route'
    valid_verbs = ['chat', 'subscribe']

    def get_subscription_channels(self, **kwargs):
        return ['chatroom']

    def chat(self, *args, **kwargs):
        errors = {}
        if 'name' not in kwargs or len(kwargs['name']) is 0:
            errors['name'] = 'Specify a name'

        if 'message' not in kwargs or len(kwargs['message']) is 0:
            errors['message'] = 'Enter a chat message'

        if errors:
            self.send_error(errors)
        else:
            self.send({'status': 'ok'})
            self.publish(self.get_subscription_channels(), kwargs)


class MessageRouter(ModelRouter):
    serializer_class = MessageSerializer
    model = Message
    route_name = 'message-router'
    def get_object(self, **kwargs):
        return self.model.objects.get(pk=kwargs['pk'])

    def get_query_set(self, **kwargs):
        return self.model.all()


route_handler.register(ChatRouter)
route_handler.register(MessageRouter)
