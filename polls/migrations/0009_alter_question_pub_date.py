# Generated by Django 3.2.7 on 2021-10-05 19:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_alter_question_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 5, 19, 5, 55, 176333, tzinfo=utc), verbose_name='date published'),
        ),
    ]
