# Generated by Django 2.2.1 on 2019-06-12 05:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passionProjectApp', '0006_auto_20190612_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 12, 5, 1, 38, 401869)),
        ),
        migrations.AlterField(
            model_name='answer',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 12, 5, 1, 38, 401850)),
        ),
        migrations.AlterField(
            model_name='answercomment',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 12, 5, 1, 38, 402468)),
        ),
        migrations.AlterField(
            model_name='answercomment',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 12, 5, 1, 38, 402441)),
        ),
        migrations.AlterField(
            model_name='realquestion',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 12, 5, 1, 38, 399455)),
        ),
        migrations.AlterField(
            model_name='realquestion',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 12, 5, 1, 38, 399432)),
        ),
        migrations.AlterField(
            model_name='realquestioncomment',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 12, 5, 1, 38, 401223)),
        ),
        migrations.AlterField(
            model_name='realquestioncomment',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 12, 5, 1, 38, 401192)),
        ),
    ]