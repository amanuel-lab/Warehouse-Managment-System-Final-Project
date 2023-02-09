from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('addProduct/', views.addProduct, name='addProduct'),
    path('displayProduct/', views.displayProduct, name='displayProduct'),
    path('displayProduct/delete/<int:pk>/', views.delete, name='delete'),
    path('displayProduct/update/<int:pk>/', views.update, name='update'),
    path('searchProduct/', views.searchProduct, name='searchProduct'),
    path('totalpriceofProduct/', views.totalpriceofProduct, name='totalpriceofProduct'),
    path('contacts/', views.contacts, name='contacts'),
    path('contactsfinal/', views.contactsfinal, name='contactsfinal'),
    
    
] 