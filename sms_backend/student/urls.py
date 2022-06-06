
"""sms_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from student.views import UserListCreateApiView,UserUpdateApiView,ClassCreateApiView,StudentCreateApiView,AttendanceCreateUpdateApiView,SubjectCreateApiView,AssignTeacherApiView

urlpatterns = [
    path('add_user/', UserListCreateApiView.as_view(),name="add_user"),
    path('update_user/<int:pk>',UserUpdateApiView.as_view(),name="update"),
    path('add_student/',StudentCreateApiView.as_view(),name="register_student"),
    path('add_class/',ClassCreateApiView.as_view(),name="add_class"),
    path('attendence/',AttendanceCreateUpdateApiView.as_view(),name='attendence'),
    path('attendence/<int:pk>',AttendanceCreateUpdateApiView.as_view(),name='update_attendence'),
    path('subject',SubjectCreateApiView.as_view(),name="add_subject"),
    path('assign_teacher',AssignTeacherApiView.as_view(),name="assing_teacher")
]
