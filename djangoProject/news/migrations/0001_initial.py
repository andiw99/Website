# Generated by Django 3.2.7 on 2021-10-05 11:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2021, 10, 5, 11, 59, 57, 625560, tzinfo=utc), verbose_name='date published')),
                ('banner', models.ImageField(upload_to='')),
                ('article_text', models.TextField(max_length=200000)),
            ],
        ),
    ]
