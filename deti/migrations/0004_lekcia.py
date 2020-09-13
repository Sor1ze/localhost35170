# Generated by Django 3.0.7 on 2020-09-12 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deti', '0003_auto_20200912_1538'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lekcia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lekcia_title', models.CharField(db_index=True, max_length=120, verbose_name='Название лекции')),
                ('lekcia_text', models.TextField(verbose_name='Текст лекции')),
            ],
        ),
    ]
