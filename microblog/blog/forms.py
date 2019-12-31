from django import forms
from django.views.generic.edit import CreateView
from blog.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('text',)