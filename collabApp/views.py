from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def public_login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

def admin_home(request):
    return render(request,'admin_home.html')