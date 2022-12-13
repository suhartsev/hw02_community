from django.shortcuts import get_object_or_404, render
from .models import Post, Group


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    template = 'posts/index.html'
    title = 'Последние обновления на сайте'
    context = {
        'posts': posts,
        'title': title,
        
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    title = "Записи сообщества 'Группа тайных поклонников графа'"
    context = {
        'group': group,
        'posts': posts,
        'title': title,
    }
    return render(request, template, context)
