from django.shortcuts import render
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
    return render(request, 'template1.html', contex)


def post_detail(request, id):
    try:
        post = Post.published.get(id=id)
    except:
        raise Http404('No Post Found!')
    contex = {
        'post': post
    }
    return render(request, 'template2.html', contex)
