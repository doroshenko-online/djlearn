from django import forms
import re
from .models import Category, News
from django.core.exceptions import ValidationError

#Тест насвязанной формы
class NewsForm_test1(forms.Form):
    title = forms.CharField(max_length=50, label='Заголовок', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Содержимое', required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))
    #photo = forms.ImageField(upload_to=r'photos/%Y/%m/%d/')
    is_published = forms.BooleanField(label='Опубликовано', required=False, initial=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False, label='Категория', empty_label='Выберите категорию',
     widget=forms.Select(attrs={'class': 'form-control'}))

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'content', 'is_published', 'category')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category':  forms.Select(attrs={'class': 'form-control'}),
        }
    
    #дополнительная валидация поля title
    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title
