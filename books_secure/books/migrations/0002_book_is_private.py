# Generated by Django 3.2.9 on 2021-11-14 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_private',
            field=models.BooleanField(default=False, verbose_name='Is Book Private'),
        ),
    ]