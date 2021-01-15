from django.contrib.auth import get_user
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    pass
    """ user = models.OneToOneField(User, on_delete=models.CASCADE) """



class City(models.Model):
    pass


class Post(models.Model):
    pass

