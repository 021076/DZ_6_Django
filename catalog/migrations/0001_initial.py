# Generated by Django 4.2 on 2024-06-09 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=150, verbose_name='Наименование категории')),
                ('category_description', models.TextField(verbose_name='Описание категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('category_name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=150, verbose_name='Наименование продукта')),
                ('product_description', models.TextField(verbose_name='Описание продукта')),
                ('imagery', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Изображение(превью)')),
                ('cost_product', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Цена за покупку')),
                ('is_published', models.CharField(choices=[('ACTUAL', 'Актуальный'), ('DRAFT', 'Черновик'), ('CANCEL', 'Отменен')], default='ACTUAL', max_length=15, verbose_name='Статус публикации')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ('category', 'product_name'),
                'permissions': [('can_cancel_published', 'Сan cancel the publication of a product'), ('can_change_product_description', 'Сan change the product description'), ('can_change_product_category', 'Сan change the product category')],
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_number', models.IntegerField(verbose_name='Номер версии')),
                ('version_title', models.CharField(max_length=150, verbose_name='Наименование версии')),
                ('actual_version', models.BooleanField(default=True, verbose_name='Актуальная версия')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='catalog.product', verbose_name='Продукт')),
            ],
            options={
                'verbose_name': 'Версия',
                'verbose_name_plural': 'Версии',
            },
        ),
    ]