from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'chats/index.html')

def login(request):
    return render(request, 'chats/login.html')

def signup(request):
    return render(request, 'chats/signup.html')
