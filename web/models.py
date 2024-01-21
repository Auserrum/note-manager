from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Текст", default="")

    def __str__(self):
        return f'{self.title} - {self.user}'


    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
