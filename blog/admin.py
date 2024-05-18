from django.contrib import admin

from blog.models import Post


@admin.register(Post)
# регистрация с возможностью настроек отображения
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'content', 'preview', 'created_at', 'is_published', 'number_views',)
    list_filter = ('title', 'is_published')
    search_fields = ('title', 'slug', 'created_at')
