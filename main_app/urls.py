from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    # path('profile/<int:city_id>/', views.profile, name='profile'),
    # path('post/', views.posts_index, name='posts_index'),
    path('posts/<int:post_id>/', views.post, name='posts_detail')
]
