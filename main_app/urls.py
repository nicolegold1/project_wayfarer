from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('posts/', views.posts, name='posts'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
    path('profile/<int:user_id>/edit/', view.profile_edit , name='profile_edit'),
]