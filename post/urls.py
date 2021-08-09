from django.contrib import admin
from django.urls import path
from home.views import home_view
from .views import *

urlpatterns = [
    path('index', post_index),
    path('<int:id>', post_detail),
    path('create', post_create),
    path('update', post_update),
    path('delete', post_delete),
]
