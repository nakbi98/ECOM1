from django.db.models import Max,Min,Count,Avg
from unicodedata import name
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import  Prodect
from .models import  Category

from django.core.paginator import Paginator
from .models import UserRegister
from django.views.decorators.csrf import csrf_exempt
#from django.contrib.auth.models import User
#from django.contrib.auth.decorators import login_required
#from django.core.files.storage import FileSystemStorage


# Create your views here.


def index(request):

    product_object = Prodect.objects.all()
    Category_object = Category.objects.all()
  #  if request.method=="POST" :
    radio=request.GET.get('radio') 
    min=request.GET.get('min') 
    max=request.GET.get('max') 

    if radio!='' and radio is not None :

  #  recherchcategorie=
     product_object=Prodect.objects.filter(category_id=radio)
    elif min!='' and min is not None: 
     product_object=Prodect.objects.exclude(price__lt=min)
    if min!='' and min is not None and radio!='' and radio is not None:
     product_object=Prodect.objects.filter(category_id=radio).exclude(price__lt=min)    
    
     #product_object=Prodect.objects.exclude(price__gt=max)
    # product_object=Prodect.objects.exclude(price__lte=min)


   # return render(request, 'shop/index.html',{'recherchcategorie' : recherchcategorie})

    item_name=request.GET.get('item_name')
    if item_name!='' and item_name is not None:
         product_object=Prodect.objects.filter(title__icontains=item_name ) 
    paginator=Paginator(product_object, 8)     
    page = request.GET.get('page')
    product_object = paginator.get_page(page)
    return render(request, 'shop/index.html', {'product_object': product_object, 'Category_object':Category_object })





def detail (request, myid):
    product_object = Prodect.objects.get(id=myid)
    product_objet = Prodect.objects.all()

    return render(request,'shop/detail.html',{'product':product_object,'product_objet':product_objet } )


def login (request):
       


    if request.method == 'POST':
        form = UserRegister(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
           # Email = form.cleaned_data['Email']
           # Tel = form.cleaned_data['Tel']
           # password =  form.cleaned_data.get['password']
            #user = authenticate(username=username, password=password )
            #login(request,user)
            messages.success(request,f'Bienvenue,{username}, Votre Inscription est Valider')
            return HttpResponseRedirect('/')
    else:
        form = UserRegister()   
    context = {'form':form}
    return render(request,'shop/login.html',context  )

def authlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:    
            auth_login(request, user)
            user.save()
            messages.success(request,f'Bienvenue,{username}')
            return HttpResponseRedirect('/')

            return redirect('/')
    return render(request,'shop/authlogin.html',{})  


def logout_user(request):
    logout(request)
    messages.success(request,("Deconecté"))
    return redirect('/')   
       
           