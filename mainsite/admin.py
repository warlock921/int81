from django.contrib import admin
from .models import Blog,BlogType

@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')
    ordering = ('id',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','author','blog_type','create_time','last_updated_time')
    ordering = ('-create_time',)
