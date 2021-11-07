from django.contrib import admin

from .models import Article
# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    model = Article
    fieldsets = [
        (None, {"fields": ["title"]}),
        ("Banner", {"fields": ["banner"]}),
        ("Text", {"fields": ["article_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]

admin.site.register(Article)