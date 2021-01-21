from django.urls import path, include
from . import views

urlpatterns = [
    # home routes
    path('', views.homepage, name='homepage'),
    path('login/', views.login, name='login'),
    # profile routes
    path('profile/', views.profile, name='profile'),
    path('profile/<int:profile_id>/', views.profile_detail, name='profile_detail'),
    path('profile/<int:profile_id>/<int:city_id>/', views.profile_show, name='profile_show'),
    path('profile/<int:profile_id>/edit/',
         views.profile_edit, name='profile_edit'),
    # city Routes
    path('city/', views.city, name='city_index'),
    path('city/<int:city_id>/', views.city_detail, name='city_detail'),
    path('city/<int:city_id>/edit/', views.city_edit, name='city_edit'),
    # Post Routes
    # path('city/<int:city_id>/delete', views.city_delete, name='city_delete'),
    # path('post/', views.posts_index, name='posts_index'),
    path('posts/', views.posts, name='all_posts'),
    path('posts/<int:post_id>/', views.post, name='posts_detail'),
    path('posts/<int:post_id>/edit/', views.post_edit, name='post_edit'),
    path('posts/<int:post_id>/delete/', views.post_delete, name='post_delete')
    
]

