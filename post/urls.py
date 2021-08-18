from django.contrib import admin
from django.urls import path
#from home.views import home_view
from .views import *

app_name='post'

urlpatterns = [
    path('index', post_index),
    path('user_index', user_post_index, name='userindex'),
    path('<int:id>', post_detail, name='detail'),
    path('create', post_create, name='create'),
    path('<int:id>/update', post_update, name='update'),
    path('<int:id>/delete', post_delete, name='delete'),
    path('category', category_view, name='category'),
    path('category/<int:category_id>', category_index_view, name='category_index'),
]
