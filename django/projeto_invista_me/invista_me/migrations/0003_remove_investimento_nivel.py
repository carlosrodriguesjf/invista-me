# Generated by Django 4.1.4 on 2023-04-06 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("invista_me", "0002_investimento_nivel"),
    ]

    operations = [
        migrations.RemoveField(model_name="investimento", name="nivel",),
    ]
