from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from blog.models import *


# Create your views here.
def index(request):
    return HttpResponse('index')


def post_list(request):
    posts = Post.published.all()
    contex = {
        'posts': posts
    }
    return render(request, 'blog/list.html', contex)


def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    contex = {
        'post': post
    }
    return render(request, 'blog/detail.html', contex)
