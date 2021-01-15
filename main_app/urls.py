from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('posts/', views.posts, name='posts'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
    path('posts/<int:post_id>', views.posts, name='posts_detail')
]
