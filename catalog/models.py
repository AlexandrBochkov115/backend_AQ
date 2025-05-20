from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True)
    popularity = models.PositiveIntegerField(default=0)
    reliability_text = models.TextField(blank=True)
    special_notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.category.name} - {self.name}"

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/%Y/%m/%d/')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

class Specification(models.Model):
    product = models.ForeignKey(Product, related_name='specifications', on_delete=models.CASCADE)
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        unique_together = [['product', 'key']]