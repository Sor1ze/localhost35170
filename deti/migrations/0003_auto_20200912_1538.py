# Generated by Django 3.0.7 on 2020-09-12 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deti', '0002_auto_20200912_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='invetory',
            name='invetory_item',
            field=models.ManyToManyField(blank=True, related_name='inventory', to='deti.Magazin', verbose_name='Вещи'),
        ),
        migrations.AddField(
            model_name='predmet',
            name='prepod',
            field=models.ManyToManyField(blank=True, related_name='predmet', to='deti.Prepod', verbose_name='Преподаватель'),
        ),
        migrations.AddField(
            model_name='student',
            name='profes',
            field=models.ManyToManyField(blank=True, related_name='student', to='deti.Profes', verbose_name='Профессия'),
        ),
    ]
