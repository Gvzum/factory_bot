from django.core.exceptions import ObjectDoesNotExist
from telebot import TeleBot
from telebot.types import Message

from factory_bot.models import TelegramChat
from factory_bot.utils import parse_bot_token_from_message, update_telegram_chat
from src import settings

bot = TeleBot(settings.TELEGRAM_BOT_API_KEY, threaded=False)


@bot.message_handler(commands=["start"])
def send_welcome(message: Message):
    bot.reply_to(
        message,
        "Hi there, I am EchoBot. To finish your setup you need to request to /bot/token."
        "Then get the token and send this token to chat. \n"
        "e.g: token=<your_generated_token>",
    )


@bot.message_handler(func=lambda message: True)
def verify_bot_token(message: Message):
    try:
        token = parse_bot_token_from_message(message)
    except (ValueError, AttributeError, KeyError):
        bot.reply_to(message, "Invalid format of token message.")
        return

    try:
        chat = TelegramChat.objects.get(telegram_token=token)
    except ObjectDoesNotExist:
        bot.reply_to(message, "Chat doesnt exist")
        return

    update_telegram_chat(message=message, telegram_chat=chat)
    bot.reply_to(message, "Successfully authenticated chat")


def start_handle():
    bot.enable_save_next_step_handlers(delay=2)
    bot.load_next_step_handlers()
    bot.infinity_polling()
