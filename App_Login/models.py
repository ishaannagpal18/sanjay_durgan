from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin, User
from django.utils.translation import ugettext_lazy

#To Automatically create one to one objects
from django.db.models.signals import post_save
from django.dispatch import receiver




# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100, blank=False)
    fullname = models.CharField(max_length=100, blank=False)
    occupation = models.CharField(max_length=50, blank=False)
    organization = models.CharField(max_length=50, blank=False)
    contact = models.CharField(max_length=12, blank=False)
    question = models.TextField(max_length=500, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + "'s Profile"
