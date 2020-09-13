from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class SignUpForm(UserCreationForm):
  first_name_student = forms.CharField(label="Имя", required = False)
  second_name_student = forms.CharField(label="Фамилия", required = False)

  class Meta:
    model = User
    fields = ('username', 'first_name_student', 'second_name_student', 'password1', 'password2', )

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('first_name_student', 'second_name_student', 'age_student')
