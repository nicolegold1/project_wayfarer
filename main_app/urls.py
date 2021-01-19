from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('profile/<int:user_id>/edit/', views.profile_edit , name='profile_edit'),
    path('city/', views.city, name='city_index'),
    path('city/<int:city_id>/', views.city_detail, name='city_detail'),
    path('city/<int:city_id>/edit/', views.city_edit, name='city_edit'),
    # path('city/<int:city_id>/delete', views.city_delete, name='city_delete'),
    # path('profile/<int:city_id>/', views.profile, name='profile'),
    # path('post/', views.posts_index, name='posts_index'),
    path('posts/<int:post_id>/', views.post, name='posts_detail'),
    path('posts/', views.posts, name='all_posts')
]
