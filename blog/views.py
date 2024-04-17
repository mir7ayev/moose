from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count
from django.core.paginator import Paginator
from .models import (
    PostTags, Post, Comment
)


def home_view(r):
    posts = Post.objects.filter(is_published=True).annotate(total=Count('comment')).order_by('-created_at')[:4]

    context = {
        'posts': posts,
    }

    return render(r, 'index.html', context)


def blog_view(r):
    page = r.GET.get('page', 1)
    tag = r.GET.get('tag')

    if tag:
        posts = Post.objects.filter(tags=tag, is_published=True).annotate(total=Count('comment')).order_by('-created_at')
    else:
        posts = Post.objects.filter(is_published=True).annotate(total=Count('comment')).order_by('-created_at')

    paginator = Paginator(posts, 5)


    context = {
        'posts': paginator.page(page),
    }

    return render(r, 'blog.html', context)


def blog_single_view(r, pk):
    if r.method == 'POST':
        Comment.objects.create(post_id=pk, name=r.POST['name'],
                               message=r.POST['message']).save()

        return redirect(f'/blog-single/{pk}/')

    post = get_object_or_404(Post, id=pk)
    comments = Comment.objects.filter(post_id=pk).order_by('-created_at')

    context = {
        'post': post,
        'comments': comments,
        'tags': PostTags.objects.filter(post=pk)
    }

    return render(r, 'blog-single.html', context)


def about_view(r):
    return render(r, 'about.html')
