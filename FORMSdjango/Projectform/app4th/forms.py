from django import forms

class StudentForm(forms.Form):
    Stu_name =forms.CharField(max_length=50)
    Stu_city=forms.CharField(max_length=100)
    Stu_email=forms.EmailField()
    Stu_contact=forms.IntegerField()
    Stu_image=forms.ImageField()
    Stu_document=forms.FileField()