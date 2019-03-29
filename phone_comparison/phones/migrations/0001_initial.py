# Generated by Django 2.1.1 on 2019-03-25 19:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lightning', models.BooleanField(verbose_name='Разъем для подключения наушников Lightning')),
            ],
        ),
        migrations.CreateModel(
            name='Motorola',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('radio', models.BooleanField(verbose_name='FM-радио')),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50, verbose_name='Модель')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('body', models.CharField(max_length=50, verbose_name='Корпус')),
                ('display', models.CharField(max_length=50, verbose_name='Дисплей')),
                ('camera', models.CharField(max_length=50, verbose_name='Камера')),
                ('memory', models.CharField(max_length=50, verbose_name='Память')),
            ],
        ),
        migrations.CreateModel(
            name='Xiaomi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('protect_glass', models.CharField(max_length=50, verbose_name='Защитное покрытие экрана')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phones.Phone', verbose_name='Модель')),
            ],
        ),
        migrations.AddField(
            model_name='motorola',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phones.Phone', verbose_name='Модель'),
        ),
        migrations.AddField(
            model_name='apple',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phones.Phone', verbose_name='Модель'),
        ),
    ]