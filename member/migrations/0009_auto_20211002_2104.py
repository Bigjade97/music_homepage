# Generated by Django 3.2.6 on 2021-10-02 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0008_auto_20211002_2023'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ballad',
            old_name='k_album',
            new_name='album',
        ),
        migrations.RenameField(
            model_name='ballad',
            old_name='k_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='ballad',
            old_name='k_singer',
            new_name='singer',
        ),
    ]