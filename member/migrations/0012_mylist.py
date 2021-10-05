# Generated by Django 3.2.6 on 2021-10-04 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0011_remove_new_album_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mylist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.top100')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.user')),
            ],
            options={
                'verbose_name': '마이리스트',
                'verbose_name_plural': '마이리스트 목록',
                'ordering': ['-pk'],
            },
        ),
    ]
