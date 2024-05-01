from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer

class LoginView(GenericViewSet):

    def login(self, request, *args, **kwargs):
        user = authenticate(
            email=request.data.get('email'),
            password=request.data.get('password'),
        )
        if user is not None:
            return Response({ 'token': Token.objects.get(user=user).key })
        else:
            return Response({ 
                'error': 'Incorrect email/password' }, 
                status=HTTP_401_UNAUTHORIZED)
        
class AuthView(ModelViewSet):
    serializer_class = UserSerializer

    def auth(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user)   
        return Response(serializer.data)
    

class RegisterUserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CurrentUserView(APIView):
    def get(self, request):
        user = request.user
        if user.is_authenticated:
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response({'error': 'User is not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
