from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User, auth
# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']

        user_verify = auth.authenticate(username=username,password=password)
        if user_verify is not None:
            auth.login(request,user_verify)
            return redirect('home')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):
    if request.method=="POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username already Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'User already exists')
                return redirect('register')
            else:
                new_user = User.objects.create_user(username=username,email=email,password=password1)
                new_user.save()
                return redirect('login')
        else:
            messages.info(request,'Password not matched')
            return redirect('register')
        return redirect('home')
    else:
        return render(request,'register.html')
    
def logout(request):
    auth.logout(request)
    return redirect('home')
