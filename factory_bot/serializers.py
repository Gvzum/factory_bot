from rest_framework import serializers

from factory_bot.models import TelegramChat


class SendMessageSerializer(serializers.Serializer):
    message_text = serializers.CharField()
