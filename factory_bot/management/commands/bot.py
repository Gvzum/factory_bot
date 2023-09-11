from django.core.management.base import BaseCommand

from factory_bot.handlers import start_handle


class Command(BaseCommand):
    help = "Command to start telebot"

    def handle(self, *args, **kwargs):
        start_handle()
