from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
# from django.contrib.auth.decorators import login_required


# Create your views here.
# @login_required
def home(request):
    return render(request, 'chats/index.html')

def login(request):
    if request.method == 'POST':
        name= request.POST['myname']
        password = request.POST['mypassword']
        user = authenticate(request, Username=name, password=password)
        if user is not None:
            print('not none')
            login(request, user)
            return redirect('/')
        else:
            return redirect('signup')
            print('go to signup')

    else: 
        return render(request, 'chats/login.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST['myname']
        email = request.POST['myemail']
        password = request.POST['mypassword']
        try:
            user = User.objects.create_user(username=name,email=email,password=password)
            user.save()
            print('everything saved')
            login(request, user)
        except IntegrityError:
            return render(request, 'chats/signup.html',{'message':'Username already exists. Choose another one.'})
        else:
            redirect('/')
    else: 
        return render(request, 'chats/signup.html')

def logoutuser(request):
    logout(request)
    return redirect('/')
