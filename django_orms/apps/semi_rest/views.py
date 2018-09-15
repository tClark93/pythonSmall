from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import UserManager, User

def index(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'semi_rest/index.html', context)

def new(request):
    return render(request, 'semi_rest/add_user.html')

def edit(request, id):
    context = {
        'user': User.objects.get(id=id)
    }
    return render(request, 'semi_rest/edit_user.html', context)

def show(request, id):
    context = {
        'user': User.objects.get(id=id)
    }
    return render(request, 'semi_rest/user_info.html', context)

def create(request):
    if request.method =='POST':
        errors = User.objects.basic_validator(request.POST)
        if len(errors):
            for message in errors:
                messages.error(request, message)
            return redirect ('/users/new')
    newuser = User.objects.create(
        first_name=request.POST['first_name'], 
        last_name=request.POST['last_name'], 
        email=request.POST['email']
        )
    newuser.save()
    return redirect('/users/'+str(newuser.id))

def destroy(request, id):
    User.objects.get(id=id).delete()
    return redirect('/users')

def update(request,id):
    changeinfo = User.objects.get(id=id)
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for message in errors:
            messages.error(request, message)
        return redirect ('/users/'+str(changeinfo)+'/edit')
    changeinfo.first_name=request.POST['first_name']
    changeinfo.last_name=request.POST['last_name']
    changeinfo.email=request.POST['email']
    changeinfo.save()
    return redirect ('/users/'+str(changeinfo.id))
