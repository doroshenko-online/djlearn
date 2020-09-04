from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import News, Category
from .forms import *
from django.views.generic import ListView

# Create your views here.
class HomeNews(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news' # Переопределить название словаря в контексте
    #extra_context = {'title': 'Главная'} # Добавление статических данных в контекст

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    # Переопределить метод получения данных
    def get_queryset(self):
        return News.objects.filter(is_published=True)

# def index(request):
#     news = News.objects.all()
#     context = {
#         'news': news,
#         'title': 'Список новостей',
#     }
#     return render(request, 'news/index.html', context=context)

class NewsByCategory(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news' # Переопределить название словаря в контексте
    #extra_context = {'title': 'Главная'} # Добавление статических данных в контекст
    allow_empty = False # Запрещает вывод пустых списков, в случае если не найден объект в бд, то выдаст 404-ю ошибку

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context

    # Переопределить метод получения данных
    def get_queryset(self):
        return News.objects.filter(is_published=True, category=self.kwargs['category_id'])

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