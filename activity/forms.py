from django import forms
from . models import Post, Comment



class PostForm(forms.ModelForm):

    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Add post'
        })
    )

    class Meta:
        model = Post
        fields = ['title', 'localization', 'content']


class CommentForm(forms.ModelForm):

    content = forms.CharField(
        widget=forms.Textarea(attrs={
            'rows': '3',
            'placeholder': 'Add post'
        })
    )

    class Meta:
        model = Comment
        fields = ['content']