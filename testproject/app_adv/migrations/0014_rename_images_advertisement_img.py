# Generated by Django 4.1.7 on 2023-08-13 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_adv', '0013_remove_advertisement_image_advertisement_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advertisement',
            old_name='images',
            new_name='img',
        ),
    ]
