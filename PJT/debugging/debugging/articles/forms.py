from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    title = forms.CharField(label='제목')
    content = forms.CharField(label='내용', widget=forms.Textarea())
    
    class Meta:
        model = Article
        fields = ['title','content']


class CommentForm(forms.ModelForm):
    content = forms.CharField(label='댓글', widget=forms.TextInput())
    
    class Meta:
        model = Comment
        fields = ['content',]

 