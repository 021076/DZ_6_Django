from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Post(models.Model):
    objects = None
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='blog/', verbose_name='Изображение(превью)', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    number_views = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        # try:
        #     return "%s" % self.title
        # except:
        #     return "%s" % self.pk
        return f'{self.title}'

    class Meta:
        verbose_name = 'Статья'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Статьи'  # Настройка для наименования набора объектов
