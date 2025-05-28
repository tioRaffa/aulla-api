from django.contrib import admin
from .models import CourseModels, ReviewModels
# Register your models here.

@admin.register(CourseModels)
class CourseAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'url',
        'active'
    ]
    ordering = [
        '-id'
        ]
    

@admin.register(ReviewModels)
class ReviewAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'course',
        'name',
        'rating',
        'active'
    ]
    ordering = [
        '-id'
    ]