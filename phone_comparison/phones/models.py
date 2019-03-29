from django.db import models


# Create your models here.
class Phone(models.Model):
    model = models.CharField(verbose_name='Модель', max_length=50)
    price = models.PositiveIntegerField(verbose_name='Цена')
    body = models.CharField(verbose_name='Корпус', max_length=50)
    display = models.CharField(verbose_name='Дисплей', max_length=50)
    camera = models.CharField(verbose_name='Камера', max_length=50)
    memory = models.CharField(verbose_name='Память', max_length=50)


class Apple(models.Model):
    model = models.ForeignKey('Phone', on_delete=models.CASCADE, verbose_name='Модель')
    lightning = models.BooleanField(verbose_name='Разъем для подключения наушников Lightning')


class Xiaomi(models.Model):
    model = models.ForeignKey('Phone', on_delete=models.CASCADE, verbose_name='Модель')
    protect_glass = models.CharField(verbose_name='Защитное покрытие экрана', max_length=50)


class Motorola(models.Model):
    model = models.ForeignKey('Phone', on_delete=models.CASCADE, verbose_name='Модель')
    radio = models.BooleanField(verbose_name='FM-радио')


