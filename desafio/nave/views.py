import json
from django.core.exceptions import ObjectDoesNotExist


from .models import User, Naver, Project
from .serializers import UserSerializer, NaverSerializer, ProjectSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@api_view(["GET"])
@csrf_exempt
def get_users(request):
    users = User.objects.get(User.objects.all)
    serializer = UserSerializer(users, many=True)
    return JsonResponse({'users': serializer.data}, safe=False, status=status.HTTP_200_OK)    

@api_view(["POST"])
@csrf_exempt
def add_user(request):
    payload = json.loads(request.body)
    try:
        user = User.objects.create(
            username = payload['email'],
            password = payload['password']
        )

        serializer = UserSerializer(user)
        return JsonResponse({'user': serializer.data}, status=status.HTTP_201_CREATED)
    except Exception:
        return JsonResponse({'error': 'Erro do Servidor, tente mais tarde'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

