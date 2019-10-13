from django.db import models
from django.contrib.auth.models import User
import ckeditor_uploader.fields
from ckeditor_uploader.fields import RichTextUploadingField



# Create your models here.
class Category(models.Model):
    STATUS = (
        (1, 'True'),
        (0, 'False'),
    )
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=250, blank=True)
    description = models.CharField(max_length=250, blank=True)
    image = models.ImageField(upload_to='images/')
    status = models.IntegerField(choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    STATUS = (
        (1, 'True'),
        (0, 'False'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=250, blank=True)
    description = models.CharField(max_length=250, blank=True)
    image = models.ImageField(upload_to='images/')
    price = models.FloatField()
    amount = models.IntegerField()
    detail = RichTextUploadingField()
    status = models.IntegerField(choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ProductImage(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    create_at = models.DateTimeField (auto_now_add=True)
    update_at = models.DateTimeField (auto_now=True)
