from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    """Lista de posts del blog"""
    posts = Post.objects.filter(published=True)
    return render(request, 'blog/list.html', {
        'posts': posts
    })

def post_detail(request, slug):
    """Detalle de un post"""
    post = get_object_or_404(Post, slug=slug, published=True)
    return render(request, 'blog/detail.html', {
        'post': post
    })
