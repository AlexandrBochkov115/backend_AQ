from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms.models import BaseInlineFormSet
from django.utils.html import format_html
from .models import Category, Product, ProductImage, Specification

# Ограничение на максимальное количество категорий
MAX_CATEGORIES = 5


class CategoryForm(admin.ModelAdmin.form):
    def clean(self):
        cleaned_data = super().clean()
        if Category.objects.count() >= MAX_CATEGORIES and not self.instance.pk:
            raise ValidationError(f"Можно создать максимум {MAX_CATEGORIES} категорий!")
        return cleaned_data


class ProductImageFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()
        image_count = sum(
            1 for form in self.forms
            if form.cleaned_data
            and not form.cleaned_data.get('DELETE', False)
            and form.cleaned_data.get('image')
        )
        if image_count > 6:
            raise ValidationError("Можно загрузить максимум 6 изображений!")


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    formset = ProductImageFormSet
    extra = 1
    max_num = 6
    fields = ('image', 'image_preview')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="100" />', obj.image.url)
        return "Нет изображения"

    image_preview.short_description = "Превью"


class SpecificationFormSet(BaseInlineFormSet):
    def clean(self):
        super().clean()
        valid_forms = [
            form for form in self.forms
            if form.cleaned_data
               and not form.cleaned_data.get('DELETE', False)
               and form.cleaned_data.get('key')
        ]
        if len(valid_forms) > 2:
            raise ValidationError("Можно добавить максимум 2 характеристики!")


class SpecificationInline(admin.TabularInline):
    model = Specification
    formset = SpecificationFormSet
    extra = 2
    max_num = 2
    fields = ('key', 'value')
    verbose_name_plural = "Характеристики"

    def get_formset(self, request, obj=None, **kwargs):
        if obj and obj.specifications.exists():
            self.extra = 0
        return super().get_formset(request, obj, **kwargs)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'slug', 'main_image_preview')
    prepopulated_fields = {"slug": ("name",)}
    inlines = [SpecificationInline, ProductImageInline]
    readonly_fields = ('main_image_preview',)
    list_filter = ('category',)
    search_fields = ('name', 'category__name')
    fieldsets = (
        (None, {
            'fields': ('category', 'name', 'slug', 'reliability_text', 'special_notes')
        }),
        ('Главное изображение', {
            'fields': ('image', 'main_image_preview'),
            'classes': ('collapse', 'closed')
        }),
    )

    def main_image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="50" />', obj.image.url)
        return "Нет изображения"

    main_image_preview.short_description = "Превью"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    form = CategoryForm

    def has_add_permission(self, request):
        # Скрываем кнопку "Добавить" если достигнут лимит
        if Category.objects.count() >= MAX_CATEGORIES:
            return False
        return super().has_add_permission(request)