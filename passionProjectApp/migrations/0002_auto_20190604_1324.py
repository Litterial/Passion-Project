# Generated by Django 2.2.1 on 2019-06-04 18:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passionProjectApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='answer',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='answercomment',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='answercomment',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='realquestioncomment',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='realquestioncomment',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
