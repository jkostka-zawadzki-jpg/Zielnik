from django.urls import path
from . import views
from .views import (
    PostDeleteView,
    PostDetailView,
    UserPostListView,
    PostUpdateView,
    CreatePostView,
    PostListView,
)

urlpatterns = [
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('', PostListView.as_view(), name='blog-home'),
    path('post/new/', CreatePostView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
]
