# Generated by Django 5.0.7 on 2024-07-30 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_profile_location_alter_profile_profileimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(default='profile_images/1.png', upload_to='profile_images'),
        ),
    ]
