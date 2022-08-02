from . import views
from django.urls import path

app_name = 'api'

urlpatterns = [
    path('posts', views.PostsList),
    path('posts/<str:slug>', views.SinglePost),
]