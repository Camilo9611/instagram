# Generated by Django 3.0.3 on 2020-02-17 04:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gestion', '0013_auto_20200216_2251'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conjunto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentarios', models.CharField(blank=True, max_length=100, null=True)),
                ('likes', models.IntegerField(blank=True, null=True)),
                ('autor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('fotos', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gestion.Inicio')),
            ],
        ),
    ]
