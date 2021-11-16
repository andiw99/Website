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

        labels = {
            "article_text": "",
            "title": "",
            "pub_date": "",
        }

        field_classes = {
            "pub_date": forms.DateTimeField,
        }

        widgets = {
            "title": forms.TextInput(
                {
                    "placeholder": "Title",
                    "rows": 1,
                    "id": "ArticleTitle"
                }
            ),
            "pub_date": forms.DateTimeInput()
        }

        help_texts = {
            "pub_date": "Date published"
        }