from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        fields = [

            'category',
            'title',
            'description',
            'post_image',
            'price',
            'adress',

        ]
        model = Post
