# Generated by Django 5.0.7 on 2024-08-01 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_post_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='id_user',
        ),
    ]
