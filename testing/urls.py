from django.shortcuts import render
from django.urls import path

from testing.views import OutAPIView

urlpatterns = [
    path('api/testing/', OutAPIView.as_view(), name='token_obtain_pair'),
]