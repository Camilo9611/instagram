# Generated by Django 3.0.3 on 2020-02-17 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0019_auto_20200217_0948'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='nombre',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
