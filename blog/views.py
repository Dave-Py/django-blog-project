from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    return render(request, 'blog/dashboard.html')


def home(request):
    posts = Post.objects.all()
    content = {'posts':posts}
    return render(request,'blog/home.html',content)


def blog_detail(request,post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request,'blog/post_detail.html',{'post':post})