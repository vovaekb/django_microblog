from django.shortcuts import render, redirect
from blog.models import Post
from blog.forms import PostForm


def post_index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog_index.html', context)

def post_create(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('')
    else:
        context = {
            'form': form,
        }
        return render(request, 'post_form.html', context)

def post_object(request, pk):
    post = Post.objects.get(id=pk)
    context = {
        'post': post,
    }
    return render(request, 'post_object.html', context)