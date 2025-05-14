from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Employee
from django.urls import reverse_lazy
# Create your views here.

class CreateEmployeeView(CreateView):
    template_name = 'employeelist/create.html'
    model = Employee
    fields = ('no', 'name', 'salary')
    success_url = reverse_lazy('list-employee')

class ListEmployeeView(ListView):
    template_name = 'employeelist/list.html'
    model = Employee
    # queryset = Employee.objects.filter(no__gte=1003)
    paginate_by = 3

class DetailEmployeeView(ListView):
    template_name = 'employeelist/detail.html'
    model = Employee

class UpdateEmployeeView(ListView):
    template_name = 'employeelist/edit.html'
    model = Employee
    fields = ('no', 'name', 'salary')
    success_url = reverse_lazy('list-employee')

class DeleteEmployeeView(ListView):
    template_name = 'employeelist/delete_confirm.html'
    model = Employee
    success_url = reverse_lazy('list-employee')

