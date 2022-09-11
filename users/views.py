from msilib.schema import AppId
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

from .models import Users
from .serializers import UsersSerializer

class UsersView(APIView):
    
    def post(self, request):
        
        serializer = UsersSerializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        user = Users.objects.create(**serializer.validated_data)
        serializer = UsersSerializer(user)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)


