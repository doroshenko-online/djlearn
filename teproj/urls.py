from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    #path('', views.index, name='home'),
    path('', views.HomeNews.as_view(), name='home'),
    #path('category/<int:category_id>/', views.get_category, name='category'),
    path('category/<int:category_id>/', views.NewsByCategory.as_view(), name='category'),
    path('news/<int:pk>', views.ViewNews.as_view() , name='view_news'),
    path('news/add-news', views.CreateNews.as_view(), name='add-news'),
    path('test/', views.test, name='test'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)