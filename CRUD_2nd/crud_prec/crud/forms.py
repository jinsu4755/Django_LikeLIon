from django import forms
from .models import Article, Comment, Hashtag


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content", "hashtags", "image"]
        # Article에 적어둔대로 fields를 적어야한다


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]


class HashtagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = ["name"]
