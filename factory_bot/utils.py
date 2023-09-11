import requests
from telebot.types import Message
from django.core.exceptions import BadRequest

from factory_bot.models import TelegramChat
from src import settings


def send_message_to_chat(chat: TelegramChat, message: str):
    send_text = (
        "https://api.telegram.org/bot"
        + settings.TELEGRAM_BOT_API_KEY
        + "/sendMessage?chat_id="
        + str(chat.chat_id)
        + "&parse_mode=Markdown&text="
        + message
    )

    response = requests.get(send_text)
    if not response.ok:
        raise BadRequest("Cannot request telegram bot")


def parse_bot_token_from_message(message: Message) -> str:
    _, token = message.text.split("=")
    return token


def update_telegram_chat(message: Message, telegram_chat: TelegramChat):
    telegram_chat.chat_id = message.chat.id
    telegram_chat.is_active = True
    telegram_chat.save(update_fields=("chat_id", "is_active"))
