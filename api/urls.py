from . import views
from django.urls import path

app_name = 'api'

urlpatterns = [
    # POSTS URLS
    path('posts', views.PostsList),
    path('posts/new', views.CreateNewPost),
    path('posts/<str:slug>', views.SinglePost),
    path('posts/<str:slug>/comments', views.PostComments),
    path('posts/comments/<int:pk>', views.SingleComment),
    path('posts/<str:slug>/delete', views.DeletePost),
    path('posts/<str:slug>/update', views.UpdatePost),
    # USERS URLS
    path('users/signup', views.SignUp),
    path('users/update', views.UserUpdate),
    path('users/profile/<int:pk>/delete', views.DeleteUser),
    path('users/profile/<int:pk>', views.UserProfile),
    path('users/profile/update', views.UpdateProfile),
]
