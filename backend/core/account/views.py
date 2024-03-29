
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from core.account.serializer import CustomUserSerializer, LoginSerializer
from django.contrib.auth import authenticate, login, logout
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import InvalidToken
from django.db.utils import IntegrityError
from django.contrib.auth.mixins import LoginRequiredMixin

def get_tokens_for_user(user):
    """ Generates the jwt token (refresh and access) 
        and firebase authentication token.
    """
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    
class UserRegistrationView(APIView):
    def post(self, request, format='json'):
        """Creates a new patient, doctor, or admin user. """
        try:
            serializer = CustomUserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'msg':'Registration Success','data':serializer.data, 'status':status.HTTP_201_CREATED})
            return Response({'msg':'Registration not successful', 'error':serializer.errors, 'status':status.HTTP_400_BAD_REQUEST})
        except Exception:
            return Response({'msg':'Email already registered', 'error':serializer.errors, 'status':status.HTTP_401_UNAUTHORIZED})

class UserLoginView(APIView):
    """ Authenticates the user and returns, token"""
    def post(self, request, format=None):
        try:
            serializer = LoginSerializer(data=request.data)
            if serializer.is_valid():
                email = serializer.validated_data.get('email')
                password = serializer.validated_data.get('password')
                user = authenticate(email=email, password=password)
                print('user', user)
                if user is not None:
                    token = get_tokens_for_user(user)
                    login(request, user)
                    return Response({'token':token,'user':serializer.data, 'msg':'Login Success', 'status':status.HTTP_200_OK})
                return Response({'msg':'Incorrect Email or Password', 'status':status.HTTP_404_NOT_FOUND})
            else:
                return Response({'msg':'Invalid Email or Password', 'status':status.HTTP_404_NOT_FOUND})
        except ObjectDoesNotExist:
            return Response({'msg':'Invalid Email or Password', 'status':status.HTTP_404_NOT_FOUND})