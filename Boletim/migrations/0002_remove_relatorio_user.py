# Generated by Django 5.0.2 on 2024-02-26 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Boletim', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relatorio',
            name='user',
        ),
    ]