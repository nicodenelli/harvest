# Generated by Django 4.1.7 on 2023-04-19 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_alter_crop_growing_season'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crop',
            old_name='water_dependancy',
            new_name='water_dependency',
        ),
    ]
