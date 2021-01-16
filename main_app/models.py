from django.contrib.auth import get_user
from django.contrib.auth.forms import UserChangeForm
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.CharField(max_length=200)
    joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    # cities = models.ManyToManyField(City)
    # posts = models.ManyToManyField(Post, blank=True)
    # class FileType(paperclip.models.FileType):
    #     pass

    # class Attachment(paperclip.models.Attachment):
    #     pass

# need to have profile avatar in post class so i can load all posts on profile page


class City(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    flags = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # posts = models.ManyToManyField(Post, blank=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    city = models.ManyToManyField(City)

    def __str__(self):
        return f"{self.title} from {self.user}"
