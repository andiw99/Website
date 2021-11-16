from django.db import models
from django.utils import timezone
from django.contrib import admin
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published", default=timezone.now())
    banner = models.ImageField(upload_to="images/")
    article_text = models.TextField(max_length=200000)


    def __str__(self):
        return self.title

    def get_intro(self):
        try:
            return self.article_text[:225] + "..."
        except IndexError:
            return self.article_text

    def get_longer_intro(self):
        try:
            base_text = self.article_text[:325]
            i = 1
            while self.article_text[(325 + i)] != " ":
                base_text += self.article_text[325 + i]
                i += 1
            return base_text + "..."
        except IndexError:
            base_text = self.article_text
            return base_text + "..."

