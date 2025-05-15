from django.db import models


# Категория товаров
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Название категории
    slug = models.SlugField(unique=True)  # Человекочитаемый URL

    def __str__(self):
        return self.name


# Изображение товара
class ProductImage(models.Model):
    product = models.ForeignKey('Product', related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/%Y/%m/%d/')  # Путь загрузки изображения
    is_main = models.BooleanField(default=False)  # Флаг для основного изображения товара

    def __str__(self):
        return f"Image for {self.product.name}"

# Характеристика товара
class ProductCharacteristic(models.Model):

    product = models.ForeignKey('Product', related_name='characteristics', on_delete=models.CASCADE)
    key = models.CharField(max_length=255)  # Ключ характеристики (например, "Гарантия")
    value = models.CharField(max_length=255)  # Значение характеристики (например, "3 года")
    description = models.TextField(null=True, blank=True)  # Описание товара

    def __str__(self):
        return f"{self.key}: {self.value}"

# Товар
class Product(models.Model):
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)  # Связь с категорией
    name = models.CharField(max_length=255)  # Название товара


    def __str__(self):
        return self.name
