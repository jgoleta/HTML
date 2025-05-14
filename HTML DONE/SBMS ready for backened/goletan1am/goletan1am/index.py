from django.http import HttpResponse
from django.shortcuts import render

def webpage1(request):
    return render(request, 'login.html')
    #if request.method == "GET":
    #    return render(request, 'login.html')

   
    #if request.method == "POST":
    #    logout(request)  
    #    return redirect('webpage1') 

def webpage2(request):
    return render(request, 'employeesinfo.html')

def webpage3(request):
    return render(request, 'menu.html')

def webpage4(request):
    return render(request, 'payment.html')

def webpage5(request):
    return render(request, 'history.html')

def webpage6(request):
    return render(request, 'signup.html')

def webpage7(request):
    return render(request, 'customer.html')

def webpage8(request):
    return render(request, 'product.html')

def webpage9(request):
    return render(request, 'delivery.html')

def webpage10(request):
    return render(request, 'sales.html')

def webpage11(request):
    return render(request, 'supply.html')
