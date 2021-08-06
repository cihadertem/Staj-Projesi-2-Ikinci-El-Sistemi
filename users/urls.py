from django.urls import path
from .views import *


app_name = 'users'

urlpatterns = [
    path('profile', profile_view, name='profile'),
    path('login', login_view, name='login'),
    path('register', register_view, name='register'),
    path('logout', logout_view, name='logout'),
    path('logout', logout_view, name='logout'),
    path('edit', editprofile_view, name='edit'),
    path('<str:username>', user_profile_view, name='userprofile')
]
