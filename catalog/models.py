from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    objects = None
    category_name = models.CharField(max_length=150, verbose_name='Наименование категории')
    category_description = models.TextField(verbose_name='Описание категории')

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'Категория'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Категории'  # Настройка для наименования набора объектов
        ordering = ('category_name',)  # сортировка по названию категории


class Product(models.Model):
    objects = None
    product_name = models.CharField(max_length=150, verbose_name='Наименование продукта')
    product_description = models.TextField(verbose_name='Описание продукта')
    imagery = models.ImageField(upload_to='products/', verbose_name='Изображение(превью)', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    cost_product = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена за покупку')
    # auto_now_add=True - установка значение «сейчас» при первом создании объекта
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    # auto_now=True - установка значения «сейчас» каждый раз при сохранении объекта
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.product_name} {self.product_description} {self.category} {self.cost_product}'

    class Meta:
        verbose_name = 'Продукт'  # Настройка для наименования одного объекта
        verbose_name_plural = 'Продукты'  # Настройка для наименования набора объектов
        ordering = ('category', 'product_name',)  # сортировка по названию категории и по названию продукта
