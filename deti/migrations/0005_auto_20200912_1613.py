# Generated by Django 3.0.7 on 2020-09-12 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deti', '0004_lekcia'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lekcia',
            options={'verbose_name': 'Леуция', 'verbose_name_plural': 'Лекции'},
        ),
        migrations.AlterModelTable(
            name='lekcia',
            table='lekcia',
        ),
    ]
