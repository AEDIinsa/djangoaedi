from django.shortcuts import render


def index(request):
    return render(request, 'aedisite/index.html', {})

def render_static(request, filename):
    return render(request, 'aedisite/'+filename, {})

