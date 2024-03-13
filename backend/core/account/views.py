
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import smart_str, force_bytes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from core.account.serializer import CustomUserSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
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
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Registration Success','data':serializer.data, 'status':status.HTTP_201_CREATED})
        return Response({'msg':'Registration not successful', 'error':serializer.errors, 'status':status.HTTP_400_BAD_REQUEST})
       

class UserLoginView(APIView):
    """ Authenticates the user and returns, token"""
    def post(self, request, format=None):
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            token = get_tokens_for_user(user)
            serializer = CustomUserSerializer(user)
            return Response({'token':token,'user':serializer.data, 'msg':'Login Success', 'status':status.HTTP_200_OK})
        return Response({'msg':'Email or Password is not Valid', 'status':status.HTTP_404_NOT_FOUND})
    
