from django import forms

class StudentForm(forms.form):
    name= forms.CharField()
    email = forms.EmailField()
    contact = forms.IntegerField()
    image = forms.ImageField()
    resume = forms.FileField()

