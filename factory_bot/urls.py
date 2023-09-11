from django.urls import path

from factory_bot.views import GenerateBotTokenView, SendMessageView

urlpatterns = [
    path("token/", GenerateBotTokenView.as_view(), name="token"),
    path("send-message/", SendMessageView.as_view(), name="send-message"),
]
