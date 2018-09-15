from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import User, Secret
from django.db.models import Count

def index(request):
    return render(request, 'finalapp/index.html')

def main(request):
    secret = Secret.objects.all()
    context = {
        'user': User.objects.get(email=request.session['email']),
        'secrets': secret.order_by('-created_at')
    }
    print(request.session['email'])
    
    return render(request, 'finalapp/main.html',context)

def top(request):
    secret = Secret.objects.all()
    context = {
        'user': User.objects.get(email=request.session['email']),
        'secrets': Secret.objects.annotate(likecount=Count('liked_by')).order_by('-likecount')
    }
    print(request.session['email'])
    
    return render(request, 'finalapp/top_secrets.html',context)

def register(request):
    errors = User.objects.valid(request.POST)
    if len(errors):
        for message in errors:
            messages.error(request, message)
        return redirect('/')
    tempPass = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'], email=request.POST['email'],password=tempPass)
    request.session['first_name'] = request.POST['first_name']
    request.session['last_name'] = request.POST['last_name']
    request.session['email'] = request.POST['email']
    print(User.objects.all())
    return redirect('/main')

def login(request):
    if User.objects.filter(email=request.POST['email']):
        user = User.objects.get(email=request.POST['email'])
        request.session['email']=user.email
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            return redirect ('/main')
    messages.error(request, 'Username and Password do not match')
    return redirect('/')

def share(request):
    author=User.objects.get(id=request.POST['user_id'])
    Secret.objects.create(content=request.POST['secret'], written_by=author)
    return redirect('/main')

def like(request):
    author=User.objects.get(email=request.session['email'])
    secret=Secret.objects.get(id=request.POST['secret_id'])
    secret.liked_by.add(author)
    secret.save()
    return redirect('/main')

def logout(request):
    request.session.clear()
    return redirect('/')