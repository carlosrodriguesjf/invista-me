# Generated by Django 4.1.4 on 2023-04-06 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("invista_me", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="investimento",
            name="nivel",
            field=models.IntegerField(default=1),
        ),
    ]