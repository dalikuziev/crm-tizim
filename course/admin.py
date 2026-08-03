from django.contrib import admin
from .models import Subject, Teacher, Student

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('title',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'birth_date',)
    search_fields = ('first_name', 'last_name')
    list_filter = ('first_name', 'last_name')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'time',)
    search_fields = ('first_name', 'last_name', 'phone_number', 'time',)
    list_filter = ('first_name', 'last_name', 'phone_number', 'time',)
