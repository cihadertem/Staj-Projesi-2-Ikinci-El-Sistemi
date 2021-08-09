from django.contrib import admin

from .models import Category, Post


@admin.register(Category)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name','parent']

    class Meta:
        model=Category

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','description','post_image','category','created_time','adress']

    class Meta:
        model=Post
