from django.shortcuts import render, redirect
from .models import *
from django.views.generic import View
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, StudentForm
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, DetailView
# Create your views here.

def lekcias_list(request):
    lekcias= Lekcia.objects.all()
    students= Student.objects.all()
    return render(request, 'deti/lekcias_list.html',
    context={'lekcias':lekcias,
    'students':students})

class LekciaDetail(View):
    def get(self, request,slug):
        lekcia = get_object_or_404(Lekcia, slug__iexact=slug)
        return render (request, 'deti/lekcia_detail.html', context ={'lekcia':lekcia})

class StudentDetail(View):
    def get(self, request, pk):
        student=get_object_or_404(Student, pk=pk)
        magazins= Magazin.objects.all()
        dopkyrs= Dopkyrs.objects.all()
        return render(request,'deti/student/profil_student.html',
        context={'student':student,
        'magazins':magazins,
        'dopkyrs':dopkyrs})



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.student.first_name_student = form.cleaned_data.get('first_name_student')
            user.student.second_name_student = form.cleaned_data.get('second_name_student')
            user.save()
            my_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=my_password)
            login(request, user)
            return redirect('lekcias_list_url')
    else:
        form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})

class EditStudentView(View):
    template_name = "deti/student/edit_student.html"

    def dispatch(self, request, *args, **kwargs):
        form = StudentForm(instance=self.get_profile(request.user))
        if request.method == 'POST':
            form = StudentForm(request.POST, request.FILES, instance=self.get_profile(request.user))
            if form.is_valid():
                form.instance.user = request.user
                form.save()

                return redirect('lekcias_list_url')
        return render(request, self.template_name, {'form': form})

    def get_profile(self, user):
        try:
            return user.student
        except:
            return None
