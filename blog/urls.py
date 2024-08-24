from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', index, name='index'),
    path('posts/', post_list, name='post_list'),
    path('posts/<int:id>', post_detail, name='post_detail')
]
