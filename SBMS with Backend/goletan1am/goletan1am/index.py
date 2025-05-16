from django.shortcuts import render, redirect, get_object_or_404
from members.models import Member, Customer, Delivery, Payment, Order, Supply
from members.forms import SupplyForm, MemberForm, CustomerForm, DeliveryForm, PaymentForm, OrderForm


def webpage1(request):
    return render(request, 'login.html')
    #if request.method == "GET":
    #    return render(request, 'login.html')

   
    #if request.method == "POST":
    #    logout(request)  
    #    return redirect('webpage1') 

def webpage2(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('webpage2')  
    else:
        form = MemberForm()

    employees = Member.objects.all() 
    return render(request, 'employeesinfo.html', {
        'form': form,
        'employees': employees
    })

def delete_employee(request, employee_id):
    employee = get_object_or_404(Member, pk=employee_id)
    employee.delete()
    return redirect('webpage2')

def webpage3(request):
    return render(request, 'menu.html')


def webpage4(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('webpage4')
    else:
        form = PaymentForm(initial={
            'payment_id': f'P{Payment.objects.count()+1:04d}'  # Auto-generate ID
        })

    payments = Payment.objects.all()
    return render(request, 'payment.html', {
        'form': form,
        'payments': payments
    })

def delete_payment(request, payment_id):
    payment = get_object_or_404(Payment, pk=payment_id)
    payment.delete()
    return redirect('webpage4')

def webpage5(request):
    if request.method == 'POST':
        print("🔸 POST received:", request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            print("✅ VALID form")
            order = form.save(commit=False)
            product_map = {
                'Whole Chicken': 'P1',
                'Chicken Feet': 'P2',
                'Chicken Head': 'P3',
                'Chicken Liver': 'P4',
                'Chicken Intestine': 'P5',
                'Chicken Blood': 'P6',
                'Chicken Gizzard': 'P7',
            }
            product_name = form.cleaned_data.get('product_name')
            order.product_id = product_map.get(product_name, 'P0')
            order.save()
            return redirect('webpage5')
        else:
            print("❌ INVALID form")
            print(form.errors)
    else:
        form = OrderForm(initial={
            'order_id': f"O{Order.objects.count() + 1:04d}"
        })

    orders = Order.objects.all()
    return render(request, 'history.html', {
        'form': form,
        'orders': orders
    })

def delete_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order.delete()
    return redirect('webpage5')


def webpage6(request):
    return render(request, 'signup.html')

def webpage7(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('webpage7')
    else:
        form = CustomerForm()

    customers = Customer.objects.all()
    return render(request, 'customer.html', {
        'form': form,
        'customers': customers
    })

def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    customer.delete()
    return redirect('webpage7')

def webpage8(request):
    return render(request, 'product.html')

def webpage9(request):
    if request.method == 'POST':
        form = DeliveryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('webpage9')
    else:
        form = DeliveryForm()

    deliveries = Delivery.objects.all()
    return render(request, 'delivery.html', {
        'form': form,
        'deliveries': deliveries
    })

def delete_delivery(request, delivery_id):
    delivery = get_object_or_404(Delivery, pk=delivery_id)
    delivery.delete()
    return redirect('webpage9')

def webpage10(request):
    return render(request, 'sales.html')

def webpage11(request):
    if request.method == 'POST':
        form = SupplyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('webpage11')
    else:
        form = SupplyForm(initial={
            'supply_id': f"SUP{Supply.objects.count() + 1:04d}"
        })

    supplies = Supply.objects.all()
    return render(request, 'supply.html', {
        'form': form,
        'supplies': supplies
    })

def delete_supply(request, supply_id):
    supply = get_object_or_404(Supply, pk=supply_id)
    supply.delete()
    return redirect('webpage11')

