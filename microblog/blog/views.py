from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from blog.models import Post
from blog.forms import PostForm


def post_index(request: HttpRequest) -> HttpResponse:
    """
    Display a list of :model:`blog.Post`.

    **Context**
    ``posts``
        A list of :model:`blog.Post`.

    **Template:**

    :template:`blog/blog_index.html`
    """
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog_index.html', context)

def post_create(request: HttpRequest) -> HttpResponse:
    """
    Display a form for creating new :model:`blog.Post` on GET request and save :model:`blog.Post` from form data on POST request.

    **Context**
    ``form``
        A form :form:`blog.PostForm`.

    **Template:**

    :template:`blog/post_form.html`
    """
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_index')
    else:
        context = {
            'form': form,
        }
        return render(request, 'post_form.html', context)

def post_object(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Display an individual :model:`blog.Post`.

    **Context**
    ``posts``
        A list of :model:`blog.Post`.

    **Template:**

    :template:`blog/post_object.html`
    """
    post = Post.objects.get(id=pk)
    context = {
        'post': post,
    }
    return render(request, 'post_object.html', context)