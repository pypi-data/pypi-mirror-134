from django.urls import path
from .views import getCaptcha

urlpatterns = [
    path('captcha/', getCaptcha)
]
