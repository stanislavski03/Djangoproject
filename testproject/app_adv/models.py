from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
from django.contrib.auth import get_user_model
from pathlib import Path
# Create your models here.

User = get_user_model()
BASE_DIR = Path(__file__).resolve().parent.parent

class Advertisement(models.Model):
    title = models.CharField('Заголовок', max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Укажите уместен ли торг')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    img = models.ImageField('Изображение', upload_to='advertisement/')

    def __str__(self):
        return f"Advertisement(id = {self.id}, title = {self.title}, price = {self.price}, img = {self.img}"

    @admin.display(description='Дата создания')
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:%S")
            return f"Сегодня в {created_time}"

        else:
            created_time = self.created_at.time().strftime("%d.%m.%Y в %H:%M:%S")
            return f"{created_time}"

    @admin.display(description='Дата редактирования')
    def updated_date(self):
        if self.created_at.date() == timezone.now().date():
            updated_time = self.created_at.time().strftime("%H:%M:%S")
            return format_html(
                '<span style="color: green">Сегодня в {}</span>', updated_time
            )

        else:
            updated_time = self.created_at.time().strftime("%d.%m.%Y в %H:%M:%S")
            return format_html(
                '<span style="color: orange"> {} </span>', updated_time
            )

    @admin.display(description='Фото')
    def image(self):
        img_url = '/media/' + str(self.img)
        if self.img:
            return format_html(
                '<img src={} style="width:70px; height:70px;">', img_url
            )
        else:
            return


class Meta:
    db_table = "advertisements"
    app_label = 'my_blog'




