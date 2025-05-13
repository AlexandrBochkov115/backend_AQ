from django.contrib import admin
from .models import Project, ProjectDetail


class ProjectDetailInline(admin.TabularInline):
    model = ProjectDetail
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectDetailInline]
    list_display = ['title', 'address', 'is_flipped']
    search_fields = ['title', 'address']


admin.site.register(Project, ProjectAdmin)

