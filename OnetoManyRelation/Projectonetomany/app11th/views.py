from django.shortcuts import render

# Create your views here.
from .models import Student, Department

def home(req):
    ##### Forward access ######
    student = Student.objects.get(id=2)
    department = student.Stu_dep
    print(department.dep_name)
    print(department.dep_datail)


   ####### Reverse access #######
    department1 =Department.objects.get(dep_name="CSE")
    studentsinAI=department1.student_data.all()

    for student in studentsinAI:
        print(student.Stuname)