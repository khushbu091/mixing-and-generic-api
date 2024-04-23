# from django.shortcuts import render

# # Create your views here.
# from .models import Employee
# from .serializer import EmployeeSerializer
# from rest_framework import mixins
# from rest_framework import generics

# class EmployeeList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

#$$ generic  class based $$
from .models import Employee
from .serializer import EmployeeSerializer
from rest_framework import generics


class EmployeeList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
