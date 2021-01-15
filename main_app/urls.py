from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
]
