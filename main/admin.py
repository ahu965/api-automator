from django.contrib import admin

# Register your models here.
from main.models import Project


class BaseAdmin(admin.ModelAdmin):
    list_per_page = 20


class ProjectsAdmin(BaseAdmin):
    list_display = ('name', 'desc', 'created_by', 'created_at')


admin.site.register(Project, ProjectsAdmin)
