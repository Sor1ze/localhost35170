# Generated by Django 3.0.7 on 2020-09-12 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_prof', models.CharField(db_index=True, max_length=120, verbose_name='Название проффессии')),
                ('slug', models.SlugField(max_length=120, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Проффессия',
                'verbose_name_plural': 'Профессии',
                'db_table': 'profes',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_index=True, max_length=120, verbose_name='Имя')),
                ('second_name', models.CharField(db_index=True, max_length=120, verbose_name='Фамилия')),
                ('login', models.CharField(db_index=True, max_length=120, verbose_name='Логин')),
                ('password', models.CharField(db_index=True, max_length=120, verbose_name='Пароль')),
                ('age', models.IntegerField(db_index=True, null=True, verbose_name='Цена')),
                ('photo', models.ImageField(blank=True, upload_to='images/photo', verbose_name='Фотография')),
                ('slug', models.SlugField(max_length=120, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Студент',
                'verbose_name_plural': 'Студенты',
                'db_table': 'student',
            },
        ),
    ]
