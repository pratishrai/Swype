from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# Index Function
def index(request):
    return render(request, 'index.html')


def employee(request):
    return render(request, 'employee.html')


def employer(request):
    return render(request, 'employer.html')
