from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Products
from .forms import ProductsForm
from .filters import filterProducts




# Create your views here.


@login_required(login_url='login')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def addProduct(request):
    if request.method =='POST':
        name = request.POST['productname']
        category = request.POST['productcategory']
        quantity = request.POST['productquantity']
        price = request.POST['productprice']

        new_product = Products(name = name, category = category, quantity = quantity, price = price)
        new_product.save()

    return render(request, 'addProduct.html')

@login_required(login_url='login')
def displayProduct(request):
    items = Products.objects.all() # using ORM
    # items = Products.objects.raw('SELECT * FROM displayProduct')  -> for using SQL
    context = {
        'items': items,
        
    }
    return render(request, 'displayProduct.html', context)

def delete(request, pk):
    remove = Products.objects.get(id=pk)
    if request.method == 'POST':
        remove.delete()
        return redirect ('displayProduct')
    return render(request, 'delete.html')

def update(request, pk):
    product = Products.objects.get(id=pk)
    form = ProductsForm(instance=product)
    if request.method == 'POST':
        form = ProductsForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('displayProduct')

    context = {
        'form':form,
    }
    return render(request, 'update.html', context)






@login_required(login_url='login')
def searchProduct(request):
    product = Products.objects.all()
    filters = filterProducts(request.GET, queryset=product)

    context = {
        'filters' : filters
    }
    return render(request, 'searchProduct.html', context)






@login_required(login_url='login')
def totalpriceofProduct(request,self):
    price = self.product.price
    quantity = self.quantity
    total = price*quantity
    
    print(total)
    
    return render(request, 'totalpriceofProduct.html')








@login_required(login_url='login')
def contacts(request):
    if request.method == "POST":
        contacts=contacts()
        name=request.POST.get('name')
        email=request.POST.get('emal')
        message=request.POST,get('message')

        contacts.name = name
        contacts.email = email
        contacts.message = message
        contacts.save()
        return redirect ('displayProduct')

    return render(request, 'contacts.html')





@login_required(login_url='login')
def contactsfinal(request):
     return render(request, 'contactsfinal.html')
