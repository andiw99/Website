# Generated by Django 3.2.7 on 2021-10-05 12:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_article_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 5, 12, 26, 51, 847107, tzinfo=utc), verbose_name='date published'),
        ),
    ]
