from django.db import models


# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published_data = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name='Рубрика')

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-published_data']


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'
        ordering = ['name']


class Spare(models.Model):
    name = models.CharField(max_length=40)


class Machine(models.Model):
    name = models.CharField(max_length=30)
    spares = models.ManyToManyField('Spare', through='Kit', through_fields=('machine', 'spare'))


class Kit(models.Model):
    machine = models.ForeignKey('Machine', on_delete=models.CASCADE)
    spare = models.ForeignKey('Spare', on_delete=models.CASCADE)
    count = models.IntegerField()
