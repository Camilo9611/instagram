# Generated by Django 3.0.3 on 2020-02-25 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0029_auto_20200225_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='inicio',
            name='slug',
            field=models.SlugField(default=None, unique=True),
        ),
    ]
