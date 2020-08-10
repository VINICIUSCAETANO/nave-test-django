from rest_framework import serializers
from .models import User, Naver, Project

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'added_by']

class NaverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Naver
        fields = ['id', 'name', 'birthdate', 'admission_date', 'job_role', 'projects', 'added_by']