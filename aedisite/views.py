from django.shortcuts import render

def render_static(request, filename):
    return render(request, 'aedisite/'+filename, {})

