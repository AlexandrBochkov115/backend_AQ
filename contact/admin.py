from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'created_at')
    search_fields = ('full_name', 'phone_number')
    list_filter = ('created_at',)