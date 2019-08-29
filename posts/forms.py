from django import forms
from .models import Post

class BlogPostForm(forms.ModelForm):
    model = Post
    fields = ('title', 'content', 'published_date', 'image', 'tag')