from django.shortcuts import render
from .models import Product
from .form import ProductForm

# Create your views here.
def index(request):
    items = Product.objects.all()
    
    context = {
        "items":items
    }
    
   
   
    return render(request,"index.html",context)

def add_product(request):
  
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    
    
    
    context = {
        "form":form
    }
   
    return render(request,"create.html",context)
def update(request,pk):
    item = Product.objects.get(id=pk)
    form = ProductForm(instance=item)
    if request.method == "POST":
        form = ProductForm(request.POST,instance=item, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    
    
    
    context = {
        "form":form
    }
   
    return render(request,"update.html",context)

def delete(request, pk):
    item = Product.objects.get(id=pk)
    item.delete()
    redirect("/")