from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='loginPage'),
    path('menu/', views.menuPage, name='menuPage'),
    path('employeesinfo/', views.employeesInfoPage, name='employeesInfoPage'),
    path('customer/', views.customerInfoPage, name='customerInfoPage'),
    path('product/', views.productPage, name='productPage'),
    path('delivery/', views.deliveryPage, name='deliveryPage'),
    path('sales/', views.salesPage, name='salesPage'),
    path('supply/', views.supplyPage, name='supplyPage'),
]