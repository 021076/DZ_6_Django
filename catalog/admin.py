from django.contrib import admin
from catalog.models import Category, Product, Version


# Register your models here.
@admin.register(Category)
# регистрация с возможностью настроек отображения
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name',)
    # вывод в список отображения id и название категории


@admin.register(Product)
# регистрация с возможностью настроек отображения
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'cost_product', 'category',)
    # вывод в список отображения id, название продукта, цены и название категории
    list_filter = ('category',)
    # фильтровать по категории
    search_fields = ('product_name', 'product_description',)
    # осуществлять поиск по названию и полю описания


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('product', 'version_number', 'version_title', 'actual_version',)
    list_filter = ('product', 'actual_version')
    search_fields = ('product', 'actual_version')
