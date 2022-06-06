from operator import ge
from django.shortcuts import render
from rest_framework import generics
from student.models import user_model,classes_model,student_realtions,attendence,subject,teacher_relations
from student.serializers import  AttendenceSerilizer, UserSerializers,ClassSerilizer,StudentSerilizer,SubjectSerilizer,TeacherAssignSerializer
from rest_framework.response import Response
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

class AttendanceCreateUpdateApiView(generics.ListCreateAPIView,generics.UpdateAPIView):
    queryset = attendence.objects.all()
    serializer_class = AttendenceSerilizer

class SubjectCreateApiView(generics.ListCreateAPIView):
    queryset = subject.objects.all()
    serializer_class = SubjectSerilizer

class AssignTeacherApiView(generics.ListCreateAPIView):
    queryset = teacher_relations.objects.all()
    serializer_class = TeacherAssignSerializer
