# Generated by Django 4.1.7 on 2023-04-20 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_remove_crop_user_remove_equipment_user_crop_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='vote',
        ),
        migrations.RemoveField(
            model_name='equipment',
            name='fuel_type',
        ),
        migrations.AlterField(
            model_name='animal',
            name='preferred_living_conditions',
            field=models.CharField(max_length=250),
        ),
    ]
