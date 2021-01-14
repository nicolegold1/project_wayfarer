from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class City(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    pass


class Post(models.Model):
    title = models.CharField(max_length=20)
    field = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)
    pass


class Meta:
    ordering = ['-date']
