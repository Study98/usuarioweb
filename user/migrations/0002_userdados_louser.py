# Generated by Django 4.0.6 on 2022-07-21 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdados',
            name='louser',
            field=models.CharField(default='registrado', max_length=30, verbose_name='Nome de Usuário'),
        ),
    ]
