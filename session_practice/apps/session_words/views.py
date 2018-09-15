from django.shortcuts import render, HttpResponse, redirect
from time import localtime, strftime

def index(request):
    if 'monkey' not in request.session:
        request.session['monkey'] = []
    context = {
        'monkey': request.session['monkey']
    }
    print(context)
    return render(request, 'session_words/index.html', context)

def add(request):
    request.session["word"] = request.POST["word"]
    if 'time' not in request.POST:
        request.session['time'] = strftime("%I:%M %p, %b %d %Y", localtime())
    if 'color' not in request.POST:
        request.session['color']='black'
    else:
        request.session["color"]=request.POST['color']
    if 'fontsize' not in request.POST:
        request.session['fontsize']='24'
    else:
         request.session['fontsize']='48'
    if 'count' not in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] += 1

    temp_list = request.session['monkey']  
    temp_list.append({"word":request.session["word"], "color":request.session["color"], "fontsize":request.session['fontsize'], "time":request.session['time']})  
    request.session['monkey'] = temp_list
    # print(request.session['monkey'])
    return redirect('/')

# def result(request):
#     context = {
#     }
#     context[count]=request.session['temp_dict']
#     print(context)
#     return render(request, 'session_words/index.html', context)

def clear(request):
    request.session.clear()
    return redirect('/')
