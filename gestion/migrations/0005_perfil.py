# Generated by Django 3.0.3 on 2020-02-16 20:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gestion', '0004_inicio_autor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagenPerfil', models.ImageField(blank=True, default='default.jpeg', upload_to='')),
                ('infoCuenta', models.CharField(max_length=100)),
                ('autor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('fotos', models.ManyToManyField(to='gestion.Inicio')),
            ],
        ),
    ]
