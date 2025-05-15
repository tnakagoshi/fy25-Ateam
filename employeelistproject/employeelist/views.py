from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Employee
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class CreateEmployeeView(LoginRequiredMixin,CreateView):
    template_name = 'employeelist/create.html'
    model = Employee
    fields = ('no', 'name', 'salary')
    success_url = reverse_lazy('list-employee')

class ListEmployeeView(LoginRequiredMixin,ListView):
    template_name = 'employeelist/list.html'
    model = Employee
    # queryset = Employee.objects.filter(no__gte=1003)
    paginate_by = 3

class DetailEmployeeView(LoginRequiredMixin,DetailView):
    template_name = 'employeelist/detail.html'
    model = Employee

class UpdateEmployeeView(LoginRequiredMixin,UpdateView):
    template_name = 'employeelist/edit.html'
    model = Employee
    fields = ('no', 'name', 'salary')
    success_url = reverse_lazy('list-employee')

class DeleteEmployeeView(LoginRequiredMixin,DeleteView):
    template_name = 'employeelist/delete_confirm.html'
    model = Employee
    success_url = reverse_lazy('list-employee')

