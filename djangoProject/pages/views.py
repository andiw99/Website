from django.shortcuts import render
from django.http import HttpResponse
from news.models import Article

# Create your views here.


def home_view(request):
    latest_article_list = Article.objects.order_by("-pub_date")[:5]
    nr_articles = len(latest_article_list)
    context = {
        "latest_article_list": latest_article_list,
        "nr_articles": nr_articles,
    }

    return render(request, template_name="pages/home.html", context=context)

def contact_view(request):
    return render(request, template_name="pages/contact.html")

def service_view(request):
    return render(request, template_name="pages/services.html")