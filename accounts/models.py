from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver
from django.db import models
import datetime


class CustomUser(AbstractUser):
    email = models.EmailField(('email address'), unique=True)
    is_customer = models.BooleanField(default=True)
    join_date = models.DateField(default=datetime.date.today)
    contact_number = models.CharField(max_length=100)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    class Meta:
        db_table = 'userprofile'

    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name='profile')
    title = models.CharField(max_length=5, blank=True)
    dob = models.DateTimeField(null=True)
    address = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=50, blank=True)
    zip = models.CharField(max_length=5, blank=True)
    profile_pic = models.ImageField(
        upload_to='profile/%Y/%m/%d', blank=True, null=True)
