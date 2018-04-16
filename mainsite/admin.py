from django.contrib import admin
from .models import Blog, BlogType, ReadNum

@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')
    ordering = ('id',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','author','blog_type','read_num','create_time','last_updated_time')
    ordering = ('-create_time',)

@admin.register(ReadNum)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('read_num', 'blog')
    # ordering = ('-create_time',)
