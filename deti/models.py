from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
# Create your models here.

#База данных


class Student(models.Model): #Таблица студентов
    first_name_student = models.CharField(max_length = 120, db_index = True, verbose_name = 'Имя')
    second_name_student = models.CharField(max_length = 120, db_index = True, verbose_name = 'Фамилия')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age_student= models.IntegerField( null=True, db_index = True, verbose_name='Возраст')
    photo_student= models.ManyToManyField('Magazin', null=True, blank = True, verbose_name = 'Аватар') #это вторичный ключ для таблицы магазина с аватарками
    coin = models.IntegerField(null= True, verbose_name='Баллы' )
    profes = models.ManyToManyField('Profes', blank=True, related_name='student', verbose_name='Профессия')

    def get_ubsalut_url(self):
        return reverse('student_detail_url', kwargs={'pk':self.pk})

    def __str__(self):
        return self.first_name_student

    class Meta:
        verbose_name='Студент'
        verbose_name_plural='Студенты'
        db_table='student'




class Profes(models.Model): #Таблица проффессии
    title_prof= models.CharField(max_length = 120, db_index = True, verbose_name = 'Название проффессии')

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name='Проффессия'
        verbose_name_plural='Профессии'
        db_table='profes'

class Magazin(models.Model): #Таблица магазина
    item_name= models.CharField(max_length=120,db_index = True,verbose_name='Название предмета')
    item_pice= models.IntegerField(verbose_name='Цена предмета')
    item_photo= models.ImageField(upload_to='images/item' , blank=True, verbose_name = 'Фото Предмета', )
    buy_or_no= models.BooleanField(verbose_name='Куплино или нет', null= True)
    activ_or_no= models.BooleanField(verbose_name='Применино или нет', null= True)

    def __str__(self):
        return self.item_name

    class Meta:
        verbose_name='Магазин'
        verbose_name_plural='Магазин'
        db_table='magazin'

# class Invetory(models.Model):
#     invetory_item= models.ManyToManyField('Magazin', blank=True, related_name='inventory', verbose_name='Вещи')
#     buy_or_no= models.BooleanField(verbose_name='Куплино или нет')
#     activ_or_no= models.BooleanField(verbose_name='Применино или нет')
#
#     def __str__(self):
#         return self.item_name
#
#     class Meta:
#         verbose_name='Инвентарь'
#         verbose_name_plural='Инвентарь'
#         db_table='invetory'

class Predmet(models.Model): #Не используется, так как все предметы храняться в магазине
    titele_predmet= models.CharField(max_length = 120, db_index = True, verbose_name = 'Название предмета')
    kol_hours= models.IntegerField(verbose_name='Количество часов')
    prepod= models.ManyToManyField('Prepod', blank=True, related_name='predmet', verbose_name='Преподаватель')



    def __str__(self):
        return self.titele_predmet

    class Meta:
        verbose_name='Предмет'
        verbose_name_plural='Предметы'
        db_table='predmet'

class Prepod(models.Model): #Таблица преподователей
    first_name_prepod = models.CharField(max_length = 120, db_index = True, verbose_name = 'Имя')
    second_name_prepod = models.CharField(max_length = 120, db_index = True, verbose_name = 'Фамилия')
    login_prepod = models.CharField(max_length = 120, db_index = True, verbose_name = 'Логин')
    password_prepod = models.CharField(max_length=120, db_index = True, verbose_name = 'Пароль')
    photo_prepod = models.ImageField(upload_to='images/student' ,blank = True, verbose_name = 'Аватар')
    slug = models.SlugField(max_length=120, unique=True, verbose_name='URL')

    def __str__(self):
        return self.first_name_prepod

    class Meta:
        verbose_name='Преподаватель'
        verbose_name_plural='Преподаватели'
        db_table='prepod'

class Lekcia(models.Model): #Таблица лекций
    lekcia_title= models.CharField(max_length = 120, db_index = True, verbose_name = 'Название лекции')
    lekcia_text= models.TextField(verbose_name='Текст лекции')
    slug = models.SlugField(max_length=120, unique=True, verbose_name='URL', blank=True)


    def get_ubsalut_url(self):
        return reverse('lekcia_detail_url', kwargs={'slug':self.slug})

    def __str__(self):
        return self.lekcia_title

    class Meta:
        verbose_name='Леуция'
        verbose_name_plural='Лекции'
        db_table='lekcia'


class Dopkyrs(models.Model):
    dopkyrs_title=  models.CharField(max_length = 120, db_index = True, verbose_name = 'Название курса')
    photo_kyrs= models.ImageField(upload_to='images/kyrs' ,blank = True, null=True, verbose_name = 'Фото курса')
    kyrs_pice= models.IntegerField(verbose_name='Цена курса')

    def __str__(self):
        return self.dopkyrs_title

    class Meta:
        verbose_name='Дополнительные курсы'
        verbose_name_plural='Дополнительные курсы'
        db_table='dopkyrs'


@receiver(post_save, sender=User)
def create_user_student(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_student(sender, instance, **kwargs):
    instance.student.save()
