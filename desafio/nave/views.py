
from .models import User, Naver, Project
from .serializers import UserSerializer, NaverSerializer, ProjectSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework import status
from rest_framework import viewsets
from django.http import request
from django.views.decorators.csrf import csrf_exempt


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer  

class NaverViewSet(viewsets.ModelViewSet):
    # queryset = Naver.objects.only(Naver.added_by.field == req.HttpRequest.body.getter(User.pk))
    # Naver.objects.filter(naver.name)
    # Naver.objects.filter(naver.job_role)
    queryset = Naver.objects.all()
    serializer_class = NaverSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated]