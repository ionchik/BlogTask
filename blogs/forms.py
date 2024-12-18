from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'text')


class BlogEditForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'text')
