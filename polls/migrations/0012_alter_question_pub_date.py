# Generated by Django 3.2.9 on 2021-11-07 17:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_alter_question_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 7, 17, 35, 54, 827403, tzinfo=utc), verbose_name='date published'),
        ),
    ]
