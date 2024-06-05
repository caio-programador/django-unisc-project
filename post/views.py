from django.shortcuts import get_object_or_404, render

from .models import Post

# Create your views here.


def initial_page(request):
    posts = Post.objects.all()
    return render(request, "post/index.html", {'posts':posts})


def post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, "post/post-detail.html", {'post':post})