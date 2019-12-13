from django.shortcuts import render
from django.http import HttpResponse
from .models import StudentsDJ, courses, enrollment, gradrates
from django.db import connection 
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

@login_required
def home(request):
    context = {'name':'Andy', 'age':'40'}
    return render(request, 'final/hello.html', context)

class Studentdetails(LoginRequiredMixin, ListView):
    template_name = 'final/student.html'
    queryset = StudentsDJ.objects.all()
    context_object_name = 'students'
    paginate_by = 10
    
class coursesClass(LoginRequiredMixin, ListView):
    template_name = 'final/courses.html'
    queryset = courses.objects.all()
    context_object_name = 'courses'
    paginate_by = 10
    
class dashboard(LoginRequiredMixin, ListView):
    template_name = 'final/dashboard.html'
    queryset = StudentsDJ.objects.all()
    context_object_name = 'students'

class gradView(LoginRequiredMixin, ListView):
    template_name = 'final/line.html'
    queryset = gradrates.objects.all()
    context_object_name = 'grads'
    
def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
    
@login_required
def enrollmentView(request):
    students_list = StudentsDJ.objects.all()
    courses_list = courses.objects.all()
    cursor = connection.cursor()    
    if 'student' not in request.session and 'course1' not in request.session:
        cursor.execute("SELECT \"LastName\" FROM final_StudentsDJ LIMIT 1")
        name = cursor.fetchone()
        request.session['student'] = name[0]
        cursor.execute("SELECT \"CourseID\" FROM final_courses LIMIT 1")
        courseID = cursor.fetchone()
        request.session['course1'] = courseID[0]
        request.session['course2'] = courseID[0]
        request.session['course3'] = courseID[0]       
    if('student' in request.GET):
        request.session['student'] = request.GET.get('student')
        request.session['course1'] = request.GET.get('course1')
        request.session['course2'] = request.GET.get('course2')
        request.session['course3'] = request.GET.get('course3')
        print(request.session['course3'])
        cursor.execute("insert into final_enrollment (\"LastName\", \"CourseID1\", \"CourseID2\", \"CourseID3\") values (%s, %s, %s, %s)",[request.session['student'], request.session['course1'], request.session['course2'], request.session['course3']])
    cursor.execute("SELECT * FROM final_enrollment WHERE \"LastName\" = %s",[request.session['student']])
    info = dictfetchall(cursor)
    students = enrollment.objects.all()
    return render(request, 'final/enrollment.html', {'students':students_list, 'courses':courses_list, 'info':info, 'students2':students})
    
    
    