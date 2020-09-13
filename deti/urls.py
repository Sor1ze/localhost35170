from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth import views

urlpatterns = [
    path('',lekcias_list, name='lekcias_list_url'),
    path('lekcia/<str:slug>', LekciaDetail.as_view(), name = 'lekcia_detail_url'),
    path('student/edit_student/', EditStudentView.as_view(), name='edit_student_url'),
    path('student/<int:pk>/',StudentDetail.as_view(), name='student_detail_url'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
]
