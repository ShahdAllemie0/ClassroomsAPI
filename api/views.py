from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView
from .serializers import RegisterSerialize

# Create your views here.

class Register(CreateAPIView):
    serializer_class = RegisterSerializer
