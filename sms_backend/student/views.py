from django.shortcuts import render
from rest_framework import generics
from student.models import user_model
from student.serializers import  UserSerializers
# Create your views here.

class StudentListCreateApiView(generics.ListCreateAPIView):
    queryset = user_model.objects.all()
    serializer_class =  UserSerializers

    def get_queryset(self):
        queryset = super(StudentListCreateApiView, self).get_queryset()
        import pdb;pdb.set_trace()
        if self.request.query_params:
            queryset = self.queryset.filter(role=self.request.query_params['role'])
            return queryset
        return self.queryset.all()
