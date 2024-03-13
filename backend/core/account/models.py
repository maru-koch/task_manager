from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from uuid import uuid4

class CustomUserManager(BaseUserManager):
    
    def create_user(self, email=None, password=None, **kwargs):
        """Creates and saves regular User with 
        the given email and password."""
        if not email:
            raise ValueError('Email is required')
        if not password:
            raise ValueError('Password is required')
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email=None, password=None, **kwargs):
        """Creates super-user. """
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_admin', True)
        if kwargs.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        if kwargs.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        
        return self.create_user(email, password, **kwargs)

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    username = None 
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]

    def __str__(self) -> str:
        return self.email
