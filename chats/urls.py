from django.urls import path
from chats.views import home,chatbot_response

urlpatterns = [
       path("/home", home, name="home"),
       path('', chatbot_response, name='chatbot_response'),
]
