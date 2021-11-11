from django.shortcuts import render
from .models import Article
from django.shortcuts import get_object_or_404
from .forms import ArticleForm
# Create your views here.


def index_view(request):
    latest_article_list = Article.objects.order_by("-pub_date")[:5]
    context = {
        "latest_article_list": latest_article_list
    }
    return render(request, "news/index.html", context)

def detail_view(request, title):
    article = get_object_or_404(Article, title=title)
    context = {
        "article": article
    }
    return render(request, "news/detail.html", context)

def create_view(request):
    print("request method:", request.method)

    form = ArticleForm(request.POST or None, request.FILES or None)

    if request.method == "POST":
        print(form.data)
        if form.is_valid():
            print("form is valid")
            form.save()
            form = ArticleForm()

    context = {
        "form": form
    }

    return render(request, "news/create.html", context)