from django.urls import path
from content.views import PostDetailAPI, PostMediaAPI, TagAnyAPI, TagCreateAPI, TagListAPI, TagListCreateAPI


urlpatterns = [
    path('tags/', TagListCreateAPI.as_view(), name='tags-list'),
    path('tags/get/', TagListAPI.as_view(), name='tags-get'),
    path('tags/post/', TagCreateAPI.as_view(), name='tags-post'),
    path('tag/<int:pk>/', TagAnyAPI.as_view(), name='tag-detail'),
    path('posts/', PostDetailAPI.as_view(), name='posts'),
    path('media/', PostMediaAPI.as_view(), name='media'),
    
]
