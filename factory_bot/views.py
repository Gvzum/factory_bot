import uuid

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from factory_bot.models import TelegramChat
from factory_bot.serializers import SendMessageSerializer
from factory_bot.utils import send_message_to_chat


class GenerateBotTokenView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        if chat := TelegramChat.objects.filter(user=request.user).last():
            return Response({"token": chat.telegram_token}, status=HTTP_201_CREATED)

        generated_telegram_token = uuid.uuid4().hex
        chat = TelegramChat.objects.create(user=request.user, telegram_token=generated_telegram_token)
        return Response({"token": chat.telegram_token}, status=HTTP_201_CREATED)


class SendMessageView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = SendMessageSerializer(data=request.data)
        if serializer.is_valid():
            chat = TelegramChat.objects.filter(user=request.user).last()
            send_message_to_chat(chat=chat, message=serializer.validated_data["message_text"])
            return Response({"msg": "Successfully sent"})

        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
