# Generated by Django 2.1.5 on 2019-02-05 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_body',
            field=models.CharField(default=' ', max_length=1000),
        ),
    ]