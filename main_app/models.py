from django.contrib.auth import get_user
from django.contrib.auth.forms import UserChangeForm
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.CharField(max_length=200)
    joined = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

    def __str__(self):
        return self.user.username
    # posts = models.ManyToManyField(Post, blank=True)
    # cities = models.ManyToManyField(City)
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
    """ posts = models.ManyToManyField(Post, blank=True)  """

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ['-created_at']
