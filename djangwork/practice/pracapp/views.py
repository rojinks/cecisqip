from django.shortcuts import render
from django.shortcuts import redirect
from pracapp.models import Post
from pracapp.forms import PostForm

def post_list(request):
    posts = Post.objects.filter(is_active=True)
    return render(request, 'pracapp/posts_list.html',{"posts":posts}) 

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'pracapp/post_detail.html', {"post":post})

def new_post(request):
    form = PostForm()
    return render(request, 'pracapp/new_post.html', {"form":form})