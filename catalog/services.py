from django.core.cache import cache
from config.settings import CACHE_ENABLED


def get_list_from_cache(model_name, key):
    """ Получение списка (продуктов, категорий) из кэша, если кэш пустой получает данные из БД"""
    if not CACHE_ENABLED:
        return model_name.objects.all()
    list_objects = cache.get(key)
    if list_objects is not None:
        return list_objects
    list_objects = model_name.objects.all()
    cache.set(key, list_objects)
    return list_objects
