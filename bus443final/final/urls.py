#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('student/', views.Studentdetails.as_view(), name="student"),
    path('course/', views.coursesClass.as_view(), name="course"),
    path('dashboard/', views.dashboard.as_view(), name="dashboard"),
    path('enrollment/', views.enrollmentView, name='enrollment'),
    path('gradrates/', views.gradView.as_view(), name='gradrates'),
]
