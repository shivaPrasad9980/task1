from django.shortcuts import render,redirect
from . models import SalesData
from .forms import SalesForm
# Create your views here.

def index(request):
    product = SalesData.objects.all()
    return render(request,'index.html',{'product':product})

def add_sales(request):
    form = SalesForm()
    if request.method == "POST":
        form = SalesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'add_sale.html',{'form':form})

def delete_sales(request,id):
    sale = SalesData.objects.get(id=id)
    sale.delete()
    return redirect('/')

def update_sales(request,id):
    sale = SalesData.objects.get(id=id)
    form = SalesForm(instance=sale)
    if request.method == "POST":
        form = SalesForm(request.POST,instance = sale)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'update_sale.html',{'form':form})