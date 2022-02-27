from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
from datetime import datetime

# Create your models here.


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self,
                    email,
                    first_name,
                    last_name,
                    password=None,
                    identity_id=None,
                    company_sign_name=None,
                    company_official_name=None,
                    company_address=None,
                    company_city=None,
                    company_district=None,
                    company_neighborhood=None,
                    company_tax_id=None,
                    company_tax_administration=None,
                    yemeksepeti_subscription=False,
                    yemeksepeti_api_secret=None,
                    yemeksepeti_api_key=None,
                    getiryemek_subscription=False,
                    getiryemek_api_secret=None,
                    getiryemek_api_key=None,
                    trendyolyemek_subscription=False,
                    trendyolyemek_api_secret=None,
                    trendyolyemek_api_key=None,
                    mobile_application_subscription=False):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name,
                          last_name=last_name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, password):
        """Create and save a new superuser with given details"""
        user = self.create_user(email, first_name, last_name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    subscription_date = models.DateTimeField(default=datetime.now)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    identity_id = models.CharField(
        max_length=20, null=True, blank=True, default=None)
    company_sign_name = models.CharField(
        max_length=255, null=True, blank=True, default=None)
    company_official_name = models.CharField(
        max_length=255, null=True, blank=True, default=None)
    company_address = models.CharField(
        max_length=500, null=True, blank=True, default=None)
    company_city = models.CharField(
        max_length=255, null=True, blank=True, default=None)
    company_district = models.CharField(
        max_length=255, null=True, blank=True, default=None)
    company_neighborhood = models.CharField(
        max_length=255, null=True, blank=True, default=None)
    company_tax_id = models.CharField(
        max_length=20, null=True, blank=True, default=None)
    company_tax_administration = models.CharField(
        max_length=255, null=True, blank=True, default=None)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    yemeksepeti_subscription = models.BooleanField(default=False)
    yemeksepeti_api_secret = models.CharField(
        max_length=255, null=True, blank=True, default=None)
    yemeksepeti_api_key = models.CharField(
        max_length=255, null=True, blank=True, default=None)
    getiryemek_subscription = models.BooleanField(default=False)
    getiryemek_api_secret = models.CharField(
        max_length=255, null=True, blank=True, default=None)
    getiryemek_api_key = models.CharField(
        max_length=255, null=True, blank=True, default=None)
    trendyolyemek_subscription = models.BooleanField(default=False)
    trendyolyemek_api_secret = models.CharField(
        max_length=255, null=True, blank=True, default=None)
    trendyolyemek_api_key = models.CharField(
        max_length=255, null=True, blank=True, default=None)
    mobile_application_subscription = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return f'{self.first_name} {self.last_name}'.title()

    def get_short_name(self):
        """Retrieve short name of user"""
        return self.first_name.title()

    def __str__(self):
        """Return string representation of user"""
        description = [self.company_sign_name,
                       self.company_official_name, f'{self.first_name} {self.last_name}', self.email]
        description = [a for a in description if a is not None]
        return ' - '.join(description)


class Platform(models.Model):
    """Platforms that supported by api"""
    platform_name = models.CharField(max_length=255)
    platform_short_name = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)
    REQUIRED_FIELDS = ['platform_name', 'platform_short_name']

    def __str__(self):
        """Return the model as a string"""
        return self.platform_name


class UserFeedItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string"""
        return f'{self.platform} - {self.status_text}'
