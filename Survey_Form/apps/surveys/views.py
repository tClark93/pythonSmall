from django.shortcuts import render, HttpResponse, redirect

def index(request):
    print('template issue')
    return render(request, 'surveys/index.html')

def process(request):
    request.session["name"] = request.POST["name"]
    request.session['dojo_location'] = request.POST['dojo_location']
    request.session['fav_lang'] = request.POST['fav_lang']
    request.session['comment'] = request.POST['comment']
    if 'count' not in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] += 1
    return redirect('/result')

def result(request):
    context = {
        "count": request.session['count'],
        "name": request.session["name"],
        "location": request.session['dojo_location'],
        "favlang": request.session['fav_lang'],
        "comment": request.session['comment'],
    }
    return render(request, 'surveys/result.html', context)

