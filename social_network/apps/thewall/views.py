from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import UserManager, User, Post, Comment

def index(request):
    return render(request, 'thewall/index.html')

def register(request):
    errors = User.objects.valid(request.POST)
    request.session['first_name'] = request.POST['first_name']
    request.session['last_name'] = request.POST['last_name']
    request.session['email'] = request.POST['email']
    if len(errors):
        for message in errors:
            messages.error(request, message)
        return redirect('/')
    tempPass = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'], email=request.POST['email'],password=tempPass)
    return redirect('/main')

def login(request):
    if User.objects.filter(email = request.POST['email']):
        user = User.objects.get(email=request.POST['email'])
        request.session['first_name']=user.first_name
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            print("password match")
            return redirect('/main')
    messages.error(request, 'Username and Password do not match')
    print ('wrong password')
    return redirect('/')

def main(request):
    context = {
        'first_name': request.session['first_name'],
        'posts': Post.objects.all(),
        'comments': Comment.objects.all()
    }
    return render(request,'thewall/main.html', context)

def post(request):
    user = User.objects.get(email=request.session['email'])
    request.session['first_name'] = user.first_name
    Post.objects.create(content=request.POST['post'], written_by=user)
    return redirect('/main')


def comment(request):
    user = User.objects.get(email=request.session['email'])
    post = Post.objects.get(id=request.POST['hidden'])
    Comment.objects.create(content=request.POST['comment'],commented_by=user,post=post)
    print(request.POST['comment'])
    return redirect('/main')

def logoff(request):
    request.session.clear()
    return redirect('/')