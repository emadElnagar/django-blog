from . import views
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='blog_list'),
    path('add-new-post', views.add_post, name='add_post'),
    path('<str:slug>', views.blog_single, name='blog_single'),
    path('edit/<str:slug>', views.update_post, name='update_post'),
    path('delete/<str:slug>', views.delete_post, name='delete_post'),
    path('like/<str:slug>', views.like_post, name='like_post'),
]
