# Generated by Django 3.0.3 on 2020-02-25 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0028_auto_20200225_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inicio',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
