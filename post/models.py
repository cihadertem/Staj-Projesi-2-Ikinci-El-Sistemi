from django.db import models
from django.urls import reverse


class Post(models.Model):
    yazar = models.ForeignKey('users.CustomUser', verbose_name='yazar', on_delete=models.CASCADE,related_name='posts')
    title = models.CharField(max_length=120,verbose_name='Başlık')
    description = models.TextField(blank=True,null=True,verbose_name='Açıklama')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL,blank=True,null=True,verbose_name='Kategori')
    post_image = models.ImageField(null=True, blank=True, default='default_product.png',verbose_name='Resim')
    created_time = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(verbose_name='Fiyat',default="1")
    adress = models.CharField(max_length=300,null=True, blank=True,default="Adres Belirtilmedi", verbose_name='Adres')
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'id': self.id})

class Category(models.Model):
    name = models.CharField(max_length=120)
    parent = models.ForeignKey('Category', on_delete=models.SET_NULL,blank=True,null=True, related_name='categories')
    def __str__(self):
        return self.name


