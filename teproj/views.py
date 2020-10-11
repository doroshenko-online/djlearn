from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import News, Category
from .forms import *
from django.views.generic import ListView, DetailView, CreateView
from .utils import MyMixin
from django.core.paginator import Paginator

# Create your views here.

def test(request):
    objects = ['John', 'Pidor', 'Dmitriy', 'Alex', 'Andrey', 'Oleg', 'Olga', 'Yura', 'Sveta']
    paginator = Paginator(objects, 2)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)
    return render(request, 'news/test.html', context={'page_obj': page_obj})

class HomeNews(MyMixin, ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news' # Переопределить название словаря в контексте
    #extra_context = {'title': 'Главная'} # Добавление статических данных в контекст
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context

    # Переопределить метод получения данных
    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category') #Жадное выполнение sql(выполняется сразу), параметром указывается поле связанной модели. prefetch для ManyToMany

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
        return News.objects.filter(is_published=True, category=self.kwargs['category_id']).select_related('category')

def get_category(request, category_id):
    news = News.objects.filter(category=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news,
        'title': category.title,
        'category': category,
    }
    return render(request, 'news/index.html', context=context)

class ViewNews(DetailView):
    model = News
    # pk_url_kwarg = 'news_id'
    template_name = 'news/news_detail.html'
    context_object_name = 'item'

class CreateNews(CreateView):
    form_class = NewsForm
    template_name = 'news/add-news.html'