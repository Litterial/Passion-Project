# Generated by Django 2.2.1 on 2019-06-11 15:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passionProjectApp', '0004_auto_20190606_1519'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 11, 15, 15, 31, 42867)),
        ),
        migrations.AlterField(
            model_name='answer',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 11, 15, 15, 31, 42848)),
        ),
        migrations.AlterField(
            model_name='answercomment',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 11, 15, 15, 31, 43384)),
        ),
        migrations.AlterField(
            model_name='answercomment',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 11, 15, 15, 31, 43359)),
        ),
        migrations.AlterField(
            model_name='realquestion',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 11, 15, 15, 31, 41738)),
        ),
        migrations.AlterField(
            model_name='realquestion',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 11, 15, 15, 31, 41715)),
        ),
        migrations.AlterField(
            model_name='realquestioncomment',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 11, 15, 15, 31, 42337)),
        ),
        migrations.AlterField(
            model_name='realquestioncomment',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 11, 15, 15, 31, 42318)),
        ),
    ]
