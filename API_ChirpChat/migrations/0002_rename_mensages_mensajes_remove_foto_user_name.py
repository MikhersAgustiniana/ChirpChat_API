# Generated by Django 4.2.1 on 2023-05-07 04:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("API_ChirpChat", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="mensages",
            new_name="mensajes",
        ),
        migrations.RemoveField(
            model_name="foto",
            name="user_name",
        ),
    ]