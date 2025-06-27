from django.shortcuts import render
# Create your views here.
from .models import Addhar,Student


# Create your views here.

def student(request):
    data = Student.objects.all()
    print(data.values())
    print("forword access-----------------")
    student = Student.objects.get(name = "Rahul")
    print(student)
    stu_to_aadhar = student.aadhar_no
    print(stu_to_aadhar.aadhar)
    print(stu_to_aadhar.createdate)
    print(stu_to_aadhar.createdby)
    # my_list = []
    # for i in all_data:
    #     name = i.stu_name
    #     email = i.stu_email
    #     contact = i.stu_contact
    #     aadhar_no = i.aadhar_no
    #     created_date = i.aadhar_no.create_date
    #     created_by = i.aadhar_no.created_by
    #     data = {
    #         'name':name,
    #         'email':email,
    #         'contact':contact,
    #         'aadhar_no':aadhar_no,
    #         'created_date':created_date,
    #         'created_by':created_by
    #     }
    #     my_list.append(data)
    # print(my_list)
    
def aadhar(request):
    all_data = Addhar.objects.all()
    print(all_data.values())
    print(all_data.values_list())
    print("reverse access------------------------- related_name='student_info'") 
    aadhar = Addhar.objects.get(aadhar='12345')
    print(aadhar)
    print(aadhar.student_info)
    print(aadhar.student_info.name)
    print(aadhar.student_info.email)
    print(aadhar.student_info.contact)
    print(aadhar.student_info.addhar_no)