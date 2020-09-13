from django.contrib import admin
from .models import *
from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# Register your models here.

class LekciaAdminForm(forms.ModelForm):
    lekcia_text = forms.CharField(label='Текст лекции', widget=CKEditorUploadingWidget())
    class Meta:
        model = Lekcia
        fields = '__all__'

class LekciaAdmin(admin.ModelAdmin):
    list_display=['lekcia_title']
    list_filter=['lekcia_title']
    search_fields=['lekcia_title']
    form = LekciaAdminForm

    class Meta:
        model=Lekcia

admin.site.register(Student)
admin.site.register(Profes)
admin.site.register(Magazin)
# admin.site.register(Invetory)
admin.site.register(Predmet)
admin.site.register(Prepod)
admin.site.register(Lekcia, LekciaAdmin)
admin.site.register(Dopkyrs)
