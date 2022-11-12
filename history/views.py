from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *
from .models import User, Monuments
from rest_framework import permissions
from django.conf import settings
import uuid
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
import random
from django.utils import timezone

class UserApi(APIView):
    """View to create a new user"""
    authentication_classes = []
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        data = request.data
        if User.objects.filter(username=data.get('username')):
            return Response({'msg': 'User with this username already existed'},status=status.HTTP_400_BAD_REQUEST)
        if User.objects.filter(email=data.get('email')):
            return Response({'msg': 'This email is already registerd'},status=status.HTTP_400_BAD_REQUEST)

        serializer = UserRegistrationSerializer(data=data)
        if serializer.is_valid():
            token = str(uuid.uuid4())
            user = serializer.save(uuid=token)
            user_data = UserSerializer(user)
            return Response(user_data.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self, request, id):
        obj = User.objects.get(id=id)
        self.check_object_permissions(self.request, obj)
        return obj

class UserLogoutApi(APIView):
    def get(self, request):
        try: 
            request.user.auth_token.delete()
            return Response({"msg":"You have successfuly logged out"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class GetCurrentUserInfoAPI(APIView):
    """View to Show the entire details of the current user"""
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            user_data = UserSerializer(user).data
            return Response(user_data, status=status.HTTP_200_OK)
        else:
            return Response({'msg': "User is not Authenticated"}, status=status.HTTP_401_UNAUTHORIZED)

class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class GetMonumentsByIdApi(APIView):
    """Get details of any user by providing the id"""
    def get_object(self, request, id):
        obj = Monuments.objects.get(id=id)
        self.check_object_permissions(self.request, obj)
        return obj

    def get(self, request, id):
        data = self.get_object(request, id=id)
        serializer = MonumentsSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RandomMonumentsApi(APIView):
    """Get details of any user by providing the id"""
    def get_object(self, request, id):
        obj = Monuments.objects.get(id=id)
        self.check_object_permissions(self.request, obj)
        return obj

    def get(self, request):
        ids = list(Monuments.objects.all().values_list('pk', flat=True))
        id = random.choice(ids)
        data = self.get_object(request, id=id)
        serializer = MonumentsSerializer(data)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CreateMonuments(APIView):

    def post(self, request):
        data = request.data
        serializer = MonumentsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            serializer = MonumentsSerializer(data)
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)