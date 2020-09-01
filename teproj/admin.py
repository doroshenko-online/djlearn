from django.contrib import admin
from .models import *
# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published', 'category')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'category')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')

admin.site.register(News, NewsAdmin)
admin.site.register(Category)