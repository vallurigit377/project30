from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView

from app.models import *

from django.http import HttpResponse
from django.urls import reverse_lazy

class Home(TemplateView):
    template_name='app/home.html'


class SchoolList(ListView):
    model=School
    context_object_name='schools'


def wish(request,n):
    return HttpResponse(f'Hai {n} How are U')



class SchoolDetail(DetailView):
    model=School
    context_object_name='Schoolobject'


class SchoolCreate(CreateView):
    model=School
    fields='__all__'

class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'


class SchoolDelete(DeleteView):
    model=School
    context_object_name='schoolobj'
    success_url=reverse_lazy('SchoolList')


