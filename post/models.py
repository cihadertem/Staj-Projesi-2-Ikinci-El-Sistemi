from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=120,verbose_name='Başlık')
    description = models.TextField(blank=True,null=True,verbose_name='Açıklama')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL,blank=True,null=True,verbose_name='Kategori')
    post_image = models.ImageField(null=True, blank=True, default='default_product.png',verbose_name='Resim')
    created_time = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(verbose_name='Fiyat',default="1")
    adress = models.CharField(max_length=300,null=True, blank=True,default="Adres Belirtilmedi")
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=120)
    parent = models.ForeignKey('Category', on_delete=models.SET_NULL,blank=True,null=True)
    def __str__(self):
        return self.name


