from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('profile/<int:id>', views.profile, name='profile'),
    path('profile/edit', views.profile_edit, name='profile_edit'),
    path('password_change', views.change_password, name='change_password'),
]
