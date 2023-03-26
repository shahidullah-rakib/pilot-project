from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CourseSerializer, UserSerializer, StudentSerializer, AdminSerializer
from .models import Course, Admin, Student
from django.contrib.auth.models import User
# Create your views here.


class CourseViewSet(viewsets.ModelViewSet):

    queryset = Course.objects.all().order_by('-id')
    serializer_class = CourseSerializer
    permission_classes = [  # permissions.IsAuthenticated,
        # permissions.DjangoModelPermissions
    ]


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().filter(is_staff=False).order_by('-id')
    serializer_class = StudentSerializer
    permission_classes = [  # permissions.IsAuthenticated,
        # permissions.DjangoModelPermissions
    ]


class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all().filter(is_staff=True).order_by('-id')
    serializer_class = AdminSerializer
    permission_classes = [  # permissions.IsAuthenticated,
        # permissions.DjangoModelPermissions
    ]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer
    permission_classes = [  # permissions.IsAuthenticated,
        # permissions.DjangoModelPermissions
    ]
