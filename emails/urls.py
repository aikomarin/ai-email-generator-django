from django.urls import path
from .views import email_generator

urlpatterns = [
    path('', email_generator, name='email_generator'),
]
