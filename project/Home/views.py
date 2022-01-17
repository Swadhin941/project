from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from .models import accounts
# Create your views here.
def home(request):
    return render (request, 'Home.html')
def login(request):
    return render(request, 'login.html')
def register(request):
    return render(request,"Register.html")
def post(request):
    return render(request,'post.html')
def log(request):
    if request.method =='POST':
        x= str(request.POST['username'])
        y= str(request.POST['password'])
        user = auth.authenticate(username= x, password=y)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid information')
            return redirect('login')
def logout(request):
    auth.logout(request)
    return redirect('/')
def regsub(request):
    if request.method=='POST':
        username= request.POST['username']
        email = request.POST['email']
        password1= request.POST['password']
        password2 = request.POST['cpassword']
        if password1 == password2:
            if User.objects.filter(email= email).exists():
                messages.info(request, 'email taken')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'username already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email,password = password1)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'password not match')
            return redirect('register')
    else:
        return render(request,'Home.html')
def cp(request):
    if request.method == 'POST':
        a= request.POST['dist_name']
        b= request.POST['description']
        c=request.POST['price']
        d=request.POST['bedroom']
        z= accounts(District=a, Description=b,Price=c,Bedrooms=d)
        z.save()
        return redirect('/')
def search(request):
    if request.method=='POST':
        
        a = request.POST['namesearch']
        b= request.POST['numbersearch'] 
        dest= accounts.objects.filter(District=a,Bedrooms=b)
        return render(request,"Home.html",{'dest':dest,'number':b})       
        