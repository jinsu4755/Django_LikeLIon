from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Article, Comment, Hashtag
from .forms import ArticleForm, CommentForm, HashtagForm


# Create your views here.


def main(request):
    articles = Article.objects.all()
    hashtags = Hashtag.objects.all()
    # Article에 모든 요소를 articles에 저장
    return render(request, "crud/main.html", {"articles": articles,"hashtags": hashtags})


def post(request):
    if request.method == "POST":  # 만약 request 타입이 post인경우
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():  # form이 유효한지 검사
            article = form.save(commit=False)  # 아직 저장하지 않음
            article.title = form.cleaned_data["title"]
            article.content = form.cleaned_data["content"]
            article.published_at = timezone.now()
            # 시간은 지금으로 저장
            article.save()  # 이제 저장한다
            form.save_m2m()
            return redirect("crud:main")
            # 다 처리하면 crud파일에 main으로 보낸다.
    else:
        form = ArticleForm()
        return render(request, "crud/post.html", {'form': form})


def detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.content = form.cleaned_data["content"]
            comment.save()
            return redirect("crud:detail", article_id)
    else:
        form = CommentForm()
        return render(request, "crud/detail.html", {'article': article, 'form': form})


def edit(request, article_id):
    artice = get_object_or_404(Article, pk=article_id)
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=artice)
        if form.is_valid():
            article = form.save(commit=False)
            article.title = form.cleaned_data["title"]
            artice.content = form.cleaned_data["content"]
            article.published_at = timezone.now()
            artice.save()
            return redirect("crud:detail", artice.id)
    else:
        form = ArticleForm(instance=artice)
        return render(request, "crud/post.html", {'form': form})


def delete(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return redirect("crud:main")


def comment_del(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return redirect("crud:detail", comment.article.id)


def comment_edit(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.content = form.cleaned_data["content"]
            comment.save()
            return redirect("crud:detail", comment.article.id)
    else:
        form = CommentForm(instance=comment)
        return render(request, "crud/post.html", {'form': form})


def hashtagform(request, hashtag=None):
    if request.method == "POST":
        form = HashtagForm(request.POST, instance=hashtag)
        if form.is_valid():
            hashtag = form.save(commit=False)
            if Hashtag.objects.filter(name=form.cleaned_data['name']):
                form = HashtagForm()
                error_message = "이미 존제하는 해시태그 입니다."
                return render(request, 'crud/hashtag.html', {'form': form, "error_message": error_message})
            else:
                hashtag.name = form.cleaned_data['name']
                hashtag.save()
                return redirect("crud:main")
    else:
        form = HashtagForm(instance=hashtag)
        return render(request, 'crud/hashtag.html', {'form': form})


def search(request, hashtag_id):
    hashtag = get_object_or_404(Hashtag, id=hashtag_id)
    hashtags = Hashtag.objects.all()
    return render(request, 'crud/search.html', {'hashtag': hashtag, 'hashtags': hashtags})
