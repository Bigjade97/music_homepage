# Generated by Django 3.2.6 on 2021-10-02 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0010_new_album_new_song'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new_album',
            name='name',
        ),
    ]
