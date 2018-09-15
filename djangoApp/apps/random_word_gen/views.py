from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    context = {
        "random": get_random_string(length=14)
    }
    if 'num' not in request.session:
        request.session['num'] = 1
    else:
        request.session['num'] += 1
    return render(request, "random_word_gen/index.html", context)
def clear(request):
    request.session.clear()
    return redirect('/')