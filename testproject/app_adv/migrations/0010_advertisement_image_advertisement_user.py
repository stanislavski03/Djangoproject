# Generated by Django 4.1.7 on 2023-08-13 15:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_adv', '0009_alter_advertisement_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='image',
            field=models.ImageField(default=1, upload_to='advertisement/', verbose_name='Изображение'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='advertisement',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
            preserve_default=False,
        ),
    ]
