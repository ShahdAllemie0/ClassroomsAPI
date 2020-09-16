from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView, RetrieveAPIView,RetrieveUpdateAPIView,DestroyAPIView
from .serializers import (RegisterSerializer, ClassroomSerializer, ClassroomDetailsSerializer, ClassroomCreateSerializer,ClassroomUpdateSerializer)
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

class UpdateClassroom(RetrieveUpdateAPIView):
	queryset = Classroom.objects.all()
	serializer_class = ClassroomUpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'

class DeleteClassroom(DestroyAPIView):
	queryset = Classroom.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'classroom_id'
