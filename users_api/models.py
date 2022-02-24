from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

# Create your models here.
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
