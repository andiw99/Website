from django import forms

from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article

        fields = [
            "title",
            "pub_date",
            "banner",
            "article_text",
        ]