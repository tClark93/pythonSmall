from django.shortcuts import render, HttpResponse, redirect
from random import randint
from time import localtime, strftime

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'result' not in request.session:
        request.session['result'] = []
    context = {
            'result': request.session['result']
        }
    print(context)
    return render(request, 'ninja_gold/index.html', context)

def process(request):
    request.session['time'] = strftime("%I:%M %p", localtime())
    if request.POST['action'] == 'farm':
        reward = randint(10,20)
        request.session['gold'] += reward
        request.session['time'] = strftime("%I:%M %p", localtime())
        temp_list = request.session['result']
        temp_list.append("Earned "+ str(reward) +' from the farm! (' +str(request.session['time'])+')')
        request.session['result'] = temp_list
    if request.POST['action'] == 'cave':
        reward = randint(5,10)
        request.session['gold'] += reward
        request.session['time'] = strftime("%I:%M %p", localtime())
        temp_list = request.session['result']
        temp_list.append("Earned "+ str(reward) +' from the cave! (' +str(request.session['time'])+')')
        request.session['result'] = temp_list
    if request.POST['action'] == 'house':
        reward = randint(2,5)
        request.session['gold'] += reward
        request.session['time'] = strftime("%I:%M %p", localtime())
        temp_list = request.session['result']
        temp_list.append("Earned "+ str(reward) +' from the house! (' +str(request.session['time'])+')')
        request.session['result'] = temp_list
    if request.POST['action'] == 'casino':
        if request.session['gold'] == 0:
            temp_list = request.session['result']
            temp_list.append("You have no money to gamble")
            request.session['result'] = temp_list
            return redirect('/')
        reward = randint(-50,50)
        request.session['gold']+= reward
        if reward < 0:
            if request.session['gold'] < 0:
                request.session['gold'] = 0
            temp_list = request.session['result']
            temp_list.append("Lost "+ str(reward) +' at the casino! (' +str(request.session['time'])+')')
            request.session['result'] = temp_list
        if reward >= 0:
            temp_list = request.session['result']
            temp_list.append("Won "+ str(reward) +' at the casino! (' +str(request.session['time'])+')')
            request.session['result'] = temp_list
    print(request.session['gold'])
    return redirect('/')

def clear(request):
    request.session.clear()
    return redirect('/')



