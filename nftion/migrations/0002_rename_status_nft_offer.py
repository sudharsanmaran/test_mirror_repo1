# Generated by Django 4.1.7 on 2023-04-24 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("nftion", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="nft",
            old_name="status",
            new_name="offer",
        ),
    ]
