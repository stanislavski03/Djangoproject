# Generated by Django 4.1.7 on 2023-08-13 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_adv', '0012_alter_advertisement_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='image',
        ),
        migrations.AddField(
            model_name='advertisement',
            name='images',
            field=models.ImageField(default='', upload_to='advertisement/', verbose_name='Изображение'),
            preserve_default=False,
        ),
    ]
