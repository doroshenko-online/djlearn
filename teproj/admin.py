from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

# Register your models here.
from django import forms
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = News
        fields = '__all__'

class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published', 'category', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'category')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')
    fields = ('title', 'created_at', 'content', 'photo', 'get_photo',  'is_published', 'category')
    readonly_fields = ('created_at', 'updated_at', 'get_photo')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75px"')
        else:
            return '-'


    get_photo.short_description = 'Миниатюра'

admin.site.register(News, NewsAdmin)
admin.site.register(Category)

admin.site.site_title = 'Управление новостями'
admin.site.site_header = 'Управление новостями'
