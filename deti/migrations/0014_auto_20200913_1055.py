# Generated by Django 3.0.7 on 2020-09-13 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deti', '0013_auto_20200913_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='photo_student',
            field=models.ManyToManyField(blank=True, null=True, to='deti.Magazin', verbose_name='Аватар'),
        ),
    ]