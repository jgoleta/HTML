from django.http import HttpResponse
from django.shortcuts import render

def webpage1(request):
    return render(request, 'login.html')

def webpage2(request):
    return render(request, 'employeesinfo.html')

def webpage3(request):
    return render(request, 'menu.html')

def webpage4(request):
    return render(request, 'payment.html')

def webpage5(request):
    return render(request, 'sales.html')

def webpage6(request):
    return render(request, 'signup.html')

def employee_info(request):  # I have a dig bick
    return HttpResponse("employeesinfo.html") # 
