from django.db import models

class StudentsDJ(models.Model):
    StudentID = models.IntegerField()
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Major = models.CharField(max_length=50)
    Year = models.CharField(max_length=50)
    GPA = models.FloatField()

# Create your models here.

class courses(models.Model):
    CourseID = models.IntegerField()
    CourseTitle = models.CharField(max_length=100)
    CourseName = models.CharField(max_length=200)
    CourseSectionCode = models.IntegerField()
    CourseDepartment = models.CharField(max_length=100)
    InstructorFullName = models.CharField(max_length=100)
    
class enrollment(models.Model):
    LastName = models.CharField(max_length=100)
    CourseID1 = models.CharField(max_length=100)
    CourseID2 = models.CharField(max_length=100)
    CourseID3 = models.CharField(max_length=100)
    
class gradrates(models.Model):
    Campus = models.CharField(max_length=100)
    GradYear = models.IntegerField()
    Year4 = models.FloatField()
    Year5 = models.FloatField()
    Year6 = models.FloatField()