from django.shortcuts import render
from aedisite.models import TaigaAccount
from django.contrib.auth.decorators import login_required
import json
from .tools.taiga import create_taiga_account

def render_static(request, filename):
    return render(request, 'aedisite/'+filename, {})

def student_portal(request):
    taiga_account = False
    if request.user.is_authenticated and TaigaAccount.objects.filter(user = request.user).exists() :
        taiga_account = True
    return render(
            request, 
            'aedisite/espace_etudiant.html',
            {'taiga_account': taiga_account})

from urllib import parse, request
from django.utils.crypto import get_random_string

@login_required(login_url='cas_ng_login')
def student_taiga_creation(request):
    context = {'taiga_account':True}
    #TODO test real creation !!
    if not TaigaAccount.objects.filter(user = request.user).exists():
        if not request.user.has_perm('aedisite.create_taiga'):
            context['taiga_account'] = False
            context["error"] = "Vous n'appartenez pas au département informatique.\
                    Merci de solliciter si besoin l'AEDI : aedi.bureau@listes.insa-lyon.fr"
        else:
            status = create_taiga_account(request.user)
            if status == 'created':
                context["success"] = "Votre compte Taiga a bien été créé. Vous allez recevoir un mail avec\
                    vos identifiants sur votre compte INSA."
            elif status == 'existing':
                context["warning"] = "Vous possédez déjà un compte Taiga."
            else:
                context['taiga_account'] = False
                context["error"] = "Une erreur est survenue pendant la création de votre compte.\
                    Merci de prevenir l'AEDI : aedi.bureau@listes.insa-lyon.fr"
    return render(
            request,
            'aedisite/espace_etudiant.html',
            context)
