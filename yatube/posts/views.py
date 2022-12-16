from django.shortcuts import get_object_or_404, render
from django.conf import settings

from .models import Post, Group


def index(request):
    posts = Post.objects.all()[:settings.LIMIT_POSTS]
    return render(request, 'posts/index.html', {'posts': posts})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:settings.LIMIT_POSTS]
    return render(request, 'posts/group_list.html', 
                  {'group': group, 'posts': posts})
