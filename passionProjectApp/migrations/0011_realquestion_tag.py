# Generated by Django 2.0.6 on 2019-07-05 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('passionProjectApp', '0010_auto_20190629_0603'),
    ]

    operations = [
        migrations.AddField(
            model_name='realquestion',
            name='tag',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]
