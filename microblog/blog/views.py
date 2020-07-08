from django.shortcuts import render
from django.http import HttpResponseRedirect
from blog.models import Post
from blog.forms import PostForm


def post_index(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect('/')
    else:
        form = PostForm()

    posts = Post.objects.all()
    context = {
        'form': form,
        'posts': posts
    }
    return render(request, 'blog_index.html', context)
