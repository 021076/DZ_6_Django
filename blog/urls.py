from django.urls import path

from blog.apps import BlogConfig
from blog.views import PostCreateView, PostListView, PostDetailView, PostUpdateView, PostDeleteView, toggle_activity

app_name = BlogConfig.name

urlpatterns = [
    path('blog/create/', PostCreateView.as_view(), name="post_create"),
    path('blog/', PostListView.as_view(), name="post_list"),
    path('blog/view/<int:pk>/', PostDetailView.as_view(), name="post_view"),
    path('blog/edit/<int:pk>/', PostUpdateView.as_view(), name="post_edit"),
    path('blog/delete/<int:pk>/', PostDeleteView.as_view(), name="post_delete"),
    path('blog/publish/<int:pk>/', toggle_activity, name="toggle_activity"),
]
