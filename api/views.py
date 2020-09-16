from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView, RetrieveAPIView
from .serializers import RegisterSerializer, ClassroomSerializer, ClassroomDetailsSerializer, ClassroomCreateSerializer
from classes.models import Classroom
# Create your views here.

class Register(CreateAPIView):
    serializer_class = RegisterSerializer

class ClassroomList(ListAPIView):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer


class ClassroomDetails(RetrieveAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomDetailsSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'

class ClassroomCreate(CreateAPIView):
    serializer_class = ClassroomCreateSerializer
    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)