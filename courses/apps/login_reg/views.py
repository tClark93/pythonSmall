from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import User, UserManager

def index(request):
    return render(request, 'login_reg/index.html')

def registration(request):
    errors = User.objects.valid(request.POST)
    request.session['first_name'] = request.POST['first_name']
    request.session['last_name'] = request.POST['last_name']
    request.session['email'] = request.POST['email']
    if len(errors):
        for message in errors:
            messages.error(request, message)
        return redirect('/socialnetwork')
    tempPass = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'], email=request.POST['email'],password=tempPass)
    return redirect('/socialnetwork/success')

def login(request):
    if User.objects.filter(email = request.POST['email']):
        user = User.objects.get(email=request.POST['email'])
        request.session['first_name']=user.first_name
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            print("password match")
            return redirect('/socialnetwork/success')
    messages.error(request, 'Username and Password do not match')
    print ('wrong password')
    return redirect('/socialnetwork')

def success(request):
    context = {
        'name': request.session['first_name']
    }
    return render(request,'login_reg/landing.html', context)