from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=50, verbose_name='заголовок')
    content = models.TextField(verbose_name='контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата изменения')
    photo = models.ImageField(upload_to=r'photos/%Y/%m/%d/', verbose_name='картинка', blank=True)
    is_published = models.BooleanField(default=False, verbose_name='опубликовано')
    category = models.ForeignKey('Category', null=True, on_delete=models.PROTECT, verbose_name='категория')

    def __str__(self):
        return self.title

    def my_fanc(self):
        return "Hello from model"

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at', 'title']

class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='категория') #db_index - устанавливает индекс полю что делает поиск быстрее по этому полю

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']