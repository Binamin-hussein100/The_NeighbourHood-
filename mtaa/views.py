from django.shortcuts import render,redirect
from django.contrib import messages
from .models import User,Business,NeigbourHood,Post
from django.http import HttpResponse
from django.contrib import auth
from .forms import NeighbourhoodForm,PostForm,BizForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required()
def index(request):
    mtaani = NeigbourHood.objects.all()
    return render(request,'index.html',{"mtaani":mtaani})


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
    
@login_required()
def get_profile(request):
    pass

@login_required()
def neighbourhood(request):
    if request.method == 'POST':
        add = NeighbourhoodForm(request.POST)
        if add.is_valid():
            add.save()
            return redirect('home')
    else:
            add=NeighbourhoodForm()
    return render(request,'mtaa.html',{'add':add})


@login_required()
def search(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        if query:
            searched = NeigbourHood.objects.filter(hood_name__icontains=query)
            print(searched)
            return render(request,'searched.html',{'searched':searched})
        else:
            print("no data found")
            return render(request,'searched.html',{})

@login_required()
def news(request):
    all_post = Post.objects.all()
    all_biz = Business.objects.all()
    
    if request.method == 'POST':
        biz = BizForm(request.POST)
        if biz.is_valid():
            biz.save()
            return redirect('news')
    else:
        biz = BizForm()
    
    if request.method == 'POST':
        new = PostForm(request.POST)
        if new.is_valid():
            new.save()
            return redirect('news')
    else:
        new = PostForm()
    return render(request,'news.html',{"new":new,"all_post":all_post,"all_biz":all_biz,"biz":biz})

@login_required()        
def logout(request):
    logout(request)
    return redirect('login')  
