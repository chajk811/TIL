from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        max_length=10,
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': '제목을 입력하세요.',
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': '내용을 입력하세요.',
                'rows': 5,
                'cols': 50,
            }
        )
    )

    class Meta:
        model = Article
        fields = '__all__'


class CommentForm(forms.ModelForm):
    content = forms.CharField(label='댓글 입력')

    class Meta:
        model = Comment
        fields = ('content', )