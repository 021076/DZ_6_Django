from django.db import models

# Create your models here.

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    # -- Наименование
    # -- Описание
    category_name = models.CharField(max_length=150, verbose_name='Наименование категории')
    category_script = models.TextField(max_length=500, verbose_name='Описание категории')

    def __str__(self):
        return f'{self.category_name} {self.category_name}'

    class Meta:
        verbose_name = 'Категория'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Категории'  # Настройка для наименования набора объектов


class Product(models.Model):
    # - Product:
    # -- Наименование
    # -- Описание
    # -- Изображение(превью)
    # -- Категория
    # -- Цена за покупку
    # -- Дата создания(записи в БД)
    # -- Дата последнего изменения(записи в БД)
    product_name = models.CharField(max_length=150, verbose_name='Наименование продукта')
    product_script = models.TextField(verbose_name='Описание продукта')
    imagery = models.ImageField(upload_to='products/', verbose_name='Изображение(превью)', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    cost_product = models.FloatField(verbose_name='Цена за покупку')
    created_at = models.DateField(verbose_name='Дата создания')
    updated_at = models.DateField(verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.product_name} {self.product_script} {self.category} {self.cost_product}'

    class Meta:
        verbose_name = 'Продукт'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Продукты'  # Настройка для наименования набора объектов
