from django.contrib import admin
from .models import Category, Product, ProductImage, ProductCharacteristic

# Регистрация модели Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')  # Поля, которые будут отображаться в списке
    search_fields = ('name',)  # Поля для поиска
    prepopulated_fields = {'slug': ('name',)}  # Автоматическое создание slug из поля name

# Регистрация модели Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')  # Поля, которые будут отображаться в списке
    list_filter = ('category',)  # Фильтрация по категориям
    search_fields = ('name',)

# Регистрация модели ProductImage
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'is_main')  # Поля для отображения
    list_filter = ('product', 'is_main')  # Фильтрация по продукту и статусу "основного" изображения

# Регистрация модели ProductCharacteristic
class ProductCharacteristicAdmin(admin.ModelAdmin):
    list_display = ('product', 'key', 'value')  # Поля для отображения
    list_filter = ('product',)  # Фильтрация по продукту
    search_fields = ('key', 'value')  # Поиск по ключу и значению характеристики

# Регистрация моделей в админке
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(ProductCharacteristic, ProductCharacteristicAdmin)
