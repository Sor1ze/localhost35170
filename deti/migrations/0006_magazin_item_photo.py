# Generated by Django 3.0.7 on 2020-09-12 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deti', '0005_auto_20200912_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='magazin',
            name='item_photo',
            field=models.ImageField(blank=True, upload_to='images/item', verbose_name='Фото Предмета'),
        ),
    ]
