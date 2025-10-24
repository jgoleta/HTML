from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user_obj = User.objects.get(email=email)
            username = user_obj.username
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('menuPage')
        except User.DoesNotExist:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'login.html')

@login_required(login_url='loginPage')
def menuPage(request):
    return render(request, 'menu.html')

@login_required(login_url='loginPage')
def employeesInfoPage(request):
    template = loader.get_template('employeesinfo.html')
    return HttpResponse(template.render())

@login_required(login_url='loginPage')
def customerInfoPage(request):
    template = loader.get_template('customer.html')
    return HttpResponse(template.render())

@login_required(login_url='loginPage')
def productPage(request):
    template = loader.get_template('product.html')
    return HttpResponse(template.render())

@login_required(login_url='loginPage')
def deliveryPage(request):
    template = loader.get_template('delivery.html')
    return HttpResponse(template.render())

@login_required(login_url='loginPage')
def salesPage(request):
    template = loader.get_template('sales.html')
    return HttpResponse(template.render())

@login_required(login_url='loginPage')
def supplyPage(request):
    template = loader.get_template('supply.html')
    return HttpResponse(template.render())