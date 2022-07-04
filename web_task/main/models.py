from django.db import models

class Task(models.Model):
    title = models.CharField('Наименование', max_length=50, help_text='Введите наименование задачи')
    task = models.TextField('Описание', help_text='Добавьте описание задачи')
    def __str__(self):
        return self.title
    category = models.CharField('Категория', max_length=10, help_text='Укажите категорию задачи')
    curentdate = models.DateTimeField(auto_now_add=True)
