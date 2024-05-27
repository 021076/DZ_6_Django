from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def raw_select(category_select):
        category_id = Category.objects.get(category_name=f'{category_select}').__dict__
        return category_id['id']

    def handle(self, *args, **options):
        categories_list = [
            {'category_name': 'Ткани',
             'category_description': 'Текстильное полотно, изготовленное на ткацком станке переплетением взаимно перпендикулярных систем нитей'},
            {'category_name': 'Фурнитура',
             'category_description': 'Вспомогательные изделия, используемые в швейном производстве'},
            {'category_name': 'Швейное оборудование',
             'category_description': 'Машины и инструменты, используемых для раскроя, пошива, отделки и влажно-тепловой обработки изделий'},
            {'category_name': 'Нитки',
             'category_description': 'Разновидность волокнистого материала - тонко скрученная пряжа, используемая для шитья одежды'},
        ]
        Category.objects.all().delete()
        categories_for_create = []
        for category in categories_list:
            categories_for_create.append(Category(**category))
        Category.objects.bulk_create(categories_for_create)

        product_list = [
            {'product_name': 'Бязь "Розы"',
             'product_description': 'Х/б ткань, набивная с рисунком "Розы", плотность 125 г/м2, ширина 1,5 м',
             'category_id': self.raw_select('Ткани'),
             'cost_product': '350.00'},
            {'product_name': 'Пуговица для шубы',
             'product_description': 'Круглая, на ножке, основной цвет серый, с розовыми стразами',
             'category_id': self.raw_select('Фурнитура'),
             'cost_product': '75.50'},
            {'product_name': 'Ножницы портновские Mr.Pen',
             'product_description': 'Нержавеющая сталь, 9,5 дюймов, для правшей',
             'category_id': self.raw_select('Швейное оборудование'),
             'cost_product': '180.00'},
            {'product_name': 'Французское лекало',
             'product_description': 'Для оформления линии проймы, оката рукава, линии талии, горловины',
             'category_id': self.raw_select('Швейное оборудование'),
             'cost_product': '400.00'},
            {'product_name': 'Нитка вощеная для кожи и обуви черная',
             'product_description': 'Круглая крученая нить вощеная 200 м, толщина 1 мм, цвет черный',
             'category_id': self.raw_select('Нитки'),
             'cost_product': '312.00'},
            {'product_name': 'Нитки Bestex, цв.157',
             'product_description': 'Полиэстер 100%, толщина 40/2, 365 м, цвет 157-топленое молоко ',
             'category_id': self.raw_select('Нитки'),
             'cost_product': '216.00'},
        ]

        Product.objects.all().delete()
        catalog_for_create = []
        for product in product_list:
            catalog_for_create.append(Product(**product))
        Product.objects.bulk_create(catalog_for_create)
