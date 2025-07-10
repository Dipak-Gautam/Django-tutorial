from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def employee_details(request, pk):
    return render(request, 'employee_detail.html')
