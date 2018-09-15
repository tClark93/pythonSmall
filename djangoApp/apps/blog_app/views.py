from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return HttpResponse("This is a placeholder to later hold all the blogs")

def new(request):
    return HttpResponse("This is a placeholder to dislay a form to create a new blog")

def create(request):
    return redirect('/')

def show(request,number):
    return HttpResponse("Placeholder to display blog " + number)

def edit(request,number):
    return HttpResponse("Placeholder to edit blog " + number)

def destroy(request,number):
    return HttpResponse("You destroyed blog " + number)


