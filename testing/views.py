from django.shortcuts import render
from rest_framework.views import APIView
from authentication.models import * 
from authentication.serializers import*
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.response import Response
import traceback

class OutAPIView(APIView):
    def post(self, request, format = None):
        try:
            print("Hello")
            return Response({'status':'Log Out Successfully'},status = status.HTTP_200_OK)
        except Exception as e:
            return Response(status = status.HTTP_400_OK)