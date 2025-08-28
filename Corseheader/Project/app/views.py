from django.shortcuts import render
from .models import Student

# Create your views here.

from .serializers import Studentserializer
from rest_framework import generics


# class StudentList(generics.ListCreateAPIView):
#     queryset =Student.objects.all()
#     serializer_class = Studentserializer


# class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = Studentserializer
from rest_framework import  viewsets
class StudentViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Student.objects.all()
    serializer_class = Studentserializer