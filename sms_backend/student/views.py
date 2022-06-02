from django.shortcuts import render
from rest_framework import generics
from student.models import user_model,classes_model,student_realtions
from student.serializers import  UserSerializers,ClassSerilizer,StudentSerilizer
# Create your views here.

class UserListCreateApiView(generics.ListCreateAPIView):
    queryset = user_model.objects.all()
    serializer_class =  UserSerializers

    def get_queryset(self):
        queryset = super(UserListCreateApiView, self).get_queryset()
        if self.request.query_params:
            queryset = queryset.filter(role=self.request.query_params['role'])
        return queryset
class UserUpdateApiView(generics.UpdateAPIView):
    queryset = user_model.objects.all()
    serializer_class =  UserSerializers


class ClassCreateApiView(generics.ListCreateAPIView):
    queryset = classes_model.objects.all()
    serializer_class = ClassSerilizer

class StudentCreateApiView(generics.ListCreateAPIView):
    queryset = student_realtions.objects.all()
    serializer_class = StudentSerilizer