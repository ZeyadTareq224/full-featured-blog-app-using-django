from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home, name='blog-home'),
    path('post/<str:pk>/', views.post_details, name='post-details'),


    path('create_post/', views.create_post, name='create-post'),
    path('update_post/<str:pk>/', views.update_post, name='update-post'),
    path('delete_post/<str:pk>/', views.delete_post, name='delete-post'),

    path('dashboard/', views.dashboard, name='dashboard'),



]