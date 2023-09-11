import uuid

from django.contrib import auth
from django.db import models


class TelegramChat(models.Model):
    telegram_token = models.CharField(max_length=255)
    chat_id = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
