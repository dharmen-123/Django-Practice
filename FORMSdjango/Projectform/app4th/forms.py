# from django import forms

# class StudentForm(forms.Form):
#     name =forms.CharField(max_length=50)
#     city=forms.CharField(max_length=100)
#     email=forms.EmailField()
#     contact=forms.IntegerField()
#     image=forms.ImageField()
#     document=forms.FileField()

from django import forms
from django.core.exceptions import ValidationError
import re
from .models import Student
# class StudentForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     city = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     contact = forms.CharField(max_length=15)
#     image = forms.ImageField()
#     document = forms.FileField()

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
    # --- Field-level validations ---
    # def clean_name(self):
    #     name = self.cleaned_data.get('name')
    #     if not name.replace(" ", "").isalpha() :
    #         raise ValidationError("Name should only contain letters and spaces.")
    #     return name
    
    # def clean_city(self):
    #     city = self.cleaned_data.get('city')
    #     if not city.replace(" ", "").isalpha() :
    #         raise ValidationError("city should only contain letters and spaces.")
    #     return city

    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if not email.lower().endswith(('@gmail.com','@yahoo.com')):
    #         raise ValidationError("Only gmail and yahoo addresses are allowed.")
        
    #     return email

    # def clean_contact(self):
    #     contact = self.cleaned_data.get('contact')
    #     if not re.match(r'^\d{10}$', contact):
    #         raise ValidationError("Contact must be a 10-digit number.")
    #     return contact

    # def clean_image(self):
    #     image = self.cleaned_data.get('image')
    #     if image and image.size > 2 * 1024 * 1024:
    #         raise ValidationError("Image size should not exceed 2MB.")
    #     elif image and not image.name.lower().endswith(('.jpeg', '.png','jpg')):
    #         raise ValidationError("Image must be either .jpeg or .png")
    #     return image

    # def clean_document(self):
    #     document = self.cleaned_data.get('document')
    #     if document and not document.name.lower().endswith(('.pdf','.doc','.docx')):
    #         raise ValidationError("Only PDF.DOC and DOCX files are allowed.")
    #     return document

    def clean(self):
        cleaned_data=super().clean()
        name = cleaned_data.get('name') 
        city = cleaned_data.get('city') 
        email = cleaned_data.get('email') 
        contact = cleaned_data.get('contact') 
        image = cleaned_data.get('image') 
        document = cleaned_data.get('document') 
        if name==None:
           raise ValidationError("Name field should not be empty")
        elif name and not name.replace(" ", "").isalpha():
           self.add_error('name',"Name should only contain letter and space")

        if city==None:
           raise ValidationError("city field should not be empty")          
        elif city and not city.replace(" ", "").isalpha():
           self.add_error('city',"City does not content any specific word use character")

        if email==None:
           raise ValidationError("email field should not be empty") 
        elif email and not email.lower().endswith(('@gmail.com','@yahoo.com')):
           self.add_error('name',"Name should only contain letter and space")

        if contact==None:
           raise ValidationError("contact field should not be empty")
        # if contact and not re.match(r'^\d{10}$',contact):        
        elif not (str(contact).isdigit() and len(str(contact)) == 10):
           self.add_error('contact', "Contact must be a 10-digit number containing only digits.")
                              
        if image and image.size > 2 * 1024 * 1024:
           self.add_error('image',"Image size should not exceed 2MB")

        if document and not document.name.lower().endswith(('.pdf', '.doc', '.docx')):
           self.add_error('document', "Only PDF, DOC, and DOCX files are allowed.")
        
        if StudentForm.is_valid(self):
            print("hyyyyy Django")