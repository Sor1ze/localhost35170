# Generated by Django 3.0.7 on 2020-09-13 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deti', '0011_delete_invetory'),
    ]

    operations = [
        migrations.AddField(
            model_name='magazin',
            name='activ_or_no',
            field=models.BooleanField(null=True, verbose_name='Применино или нет'),
        ),
        migrations.AddField(
            model_name='magazin',
            name='buy_or_no',
            field=models.BooleanField(null=True, verbose_name='Куплино или нет'),
        ),
    ]
