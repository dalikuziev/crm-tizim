from django.contrib import admin
from .models import Subject

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)
    search_fields = ('title', 'description')
    list_filter = ('title', 'description')

