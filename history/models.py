from email.mime import image
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import uuid


class  CustomAccountManager(BaseUserManager):
    def create_user(self, email, username, password,first_name,last_name, **other_fields):
    
        if not email:
            raise ValueError("Users must have email address")
        if not username:
            raise ValueError("Users must have an username")
        if not first_name:
            raise ValueError("Users must have a first_name")
        if not last_name:
            raise ValueError("Users must have a last_name")
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **other_fields)

        user.set_password(password)

        user.save()

        return user      

    def create_superuser(self, email, username, password, first_name, last_name, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser has to be assigned is_staff = True')
        
        if other_fields.get('is_superuser') is  not True:
            raise ValueError('Superuser has to be assigned is_superuser = True')

        return self.create_user(email, username, password, first_name, last_name, **other_fields)  

class User(AbstractUser):

    username = models.CharField(max_length=30, unique=True, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    password = models.CharField(max_length=500)
    first_name = models.CharField(max_length=100,null=False, blank=False)
    last_name = models.CharField(max_length=100,null=False, blank=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']

    objects = CustomAccountManager()

    def __str__(self):
        return self.username


class Monuments(models.Model):

    title = models.CharField(max_length=30, unique=True, null=False, blank=False)
    image = models.URLField(max_length=500, null=False, blank=False)
    quote = models.CharField(max_length=250)
    description = models.TextField(null=False, blank=False)
    fact1 = models.CharField(max_length=200,null=False, blank=False)
    fact2 = models.CharField(max_length=200,null=False, blank=False)
    fact3 = models.CharField(max_length=200,null=False, blank=False)
    short = models.URLField(null=False, blank=False)

    def __str__(self):
        return self.title
