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
        return self.article_text[:250] + "..."
