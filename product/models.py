from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(default='',max_length=255)
    description = models.TextField(default='')
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(default=255,max_length=255)
    price  = models.IntegerField(default=0)
    description = models.TextField(default='')
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.title