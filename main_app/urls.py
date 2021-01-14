from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('', views.homepage, name='homepage'),
    path('posts/', views.posts, name='posts')
]