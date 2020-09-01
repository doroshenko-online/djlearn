from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import News, Category
from .forms import *

# Create your views here.

def index(request):
    news = News.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
    }
    return render(request, 'news/index.html', context=context)

def get_category(request, category_id):
    news = News.objects.filter(category=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'title': category.title,
        'category': category,
    }
    return render(request, 'news/index.html', context=context)

def view_news(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news/view_news.html', context={'item': news_item, 'title': news_item.title})

def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            #obj = News.objects.create(**form.cleaned_data) # "**" - распаковка словаря
            obj = form.save()
            return redirect(obj)
    else:
        form = NewsForm()

    return render(request, 'news/add-news.html', {'form': form})