from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import CourseManager, Course

def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'catalog/index.html', context)

def remove(request, id):
    context = {
        'course': Course.objects.get(id=id)
    }
    return render(request, 'catalog/remove.html', context)

def create(request):
    if request.method=='POST':
        errors = Course.objects.basic_validator(request.POST)
        print('button works')
        if len(errors):
            for message in errors:
                messages.error(request, message)
                return redirect('/')
        newcourse = Course.objects.create(
            name=request.POST['name'],
            descrip=request.POST['descrip']
        )
        newcourse.save()
        return redirect('/')


def destroy(request, id):
    Course.objects.get(id=id).delete()
    return redirect('/')