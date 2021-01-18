from django.contrib.auth import get_user
from django.contrib.auth.forms import UserChangeForm
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    flags = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Profile(models.Model):
    joined = models.DateTimeField(auto_now_add=True)
    cities = models.ForeignKey(City, on_delete=models.CASCADE)
    # class FileType(paperclip.models.FileType):
    #     pass

    # class Attachment(paperclip.models.Attachment):
    #     pass


class Post(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


