from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from post.Forms import PostForm

from .models import Post

# Create your views here.


def initial_page(request):
    posts = Post.objects.all()
    if request.method == 'GET':
        form = PostForm()
        context = {
            'form':form,
            'posts':posts
        }
        return render(request, 'post/index.html', context=context)
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            posts = form.save()
            form = PostForm()
        
        return redirect('initial_page')
    else:
        # metodo invalido
        ...


def post(request, id):
    post = get_object_or_404(Post, id=id)
    posts = Post.objects.all()
    if request.method == 'GET':
        form = PostForm()
        context = {
            'form':form,
            'post':post
        }
        return render(request, 'post/post-detail.html', context=context)
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            posts = form.save()
            form = PostForm()
        
        return redirect(reverse('post_details', args=[post.id]))
    else:
        # metodo invalido
        ...
