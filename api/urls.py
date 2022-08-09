from . import views
from django.urls import path

app_name = 'api'

urlpatterns = [
    path('posts', views.PostsList),
    path('posts/new', views.CreateNewPost),
    path('posts/<str:slug>', views.SinglePost),
    path('posts/<str:slug>/comments', views.PostComments),
    path('posts/comments/<int:pk>', views.SingleComment),
    path('posts/<str:slug>/delete', views.DeletePost),
    path('posts/<str:slug>/update', views.UpdatePost),
]
