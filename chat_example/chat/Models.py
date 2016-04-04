from django.db import models
from swampdragon.models import SelfPublishModel

from chat_example.chat.serializers import MessageSerializer


class Message(SelfPublishModel, models.Model):
    serializer_class = MessageSerializer
    text = models.CharField(max_length=100)