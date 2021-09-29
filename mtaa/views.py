from django.shortcuts import render,redirect
from django.contrib import messages
from .models import User,Business,NeigbourHood
from django.http import HttpResponse
from django.contrib import auth

# Create your views here.
def index(request):
    return HttpResponse('WELCOME')

def register(request):
    if request.method == 'POST':
            username = request.POST['username']
            neighbourhood = request.POST['neighbourhood']
            email = request.POST['email']
            password1=request.POST['password']
            password2 = request.POST['password2']
        
            if password1 == password2:
                if User.objects.filter(username = username).exists():
                    print('already exists')    
                    return redirect('register')
                else:
                    if User.objects.filter(email=email).exists():
                        messages.add_message(request, messages.warning,'Email already exists! Try another.')
                        return redirect('register')
                    else:
                        user = User.objects.create_user(username=username,email=email,password=password1)
                        user.save()
                        return redirect('login')
            else:
                return render(request,'register.html')
    return render(request,'register.html')
        
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            messages.info(request,'Successfully logged in')
            
            return redirect('home')
        else:
            messages.warning(request, 'Save was unsuccessful.')
            return redirect('login')
        
    else:
        return render(request,'login.html')

def get_profile(request):
    pass