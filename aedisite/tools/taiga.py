from django.utils.crypto import get_random_string
from urllib import parse, request
from urllib.error import HTTPError
import json
from aedisite.models import TaigaAccount


def create_taiga_account(user):
    account = {
            "type": "public",
            "username": user.username,
            "password": get_random_string(),
            "email": user.email,
            "full_name": user.get_full_name(),
            }
    url = 'https://webaedi.insa-lyon.fr/api/api/v1/auth/register'
    data = parse.urlencode(account)
    data = data.encode('ascii') # data should be bytes
    req = request.Request(url, data)
    try:
        response = request.urlopen(req)
        welcome_email = TAIGA_MAIL%(account.get('full_name'), account.get('username'), account.get('password'))
        user.email_user('Your Taiga Account', welcome_email, 'Taiga AEDI <taiga@webaedi.insa-lyon.fr>')
        taiga_account = TaigaAccount(user=user, created=True)
        taiga_account.save()
        return 'created'
    except HTTPError as err:
        if err.code == 400:
            error_messages = json.loads(err.read().decode('utf-8'))
            if error_messages.get('_error_type') == "taiga.base.exceptions.WrongArguments":
                taiga_account = TaigaAccount(user=user, created=False)
                taiga_account.save()
                return 'existing'
    return 'error'

TAIGA_MAIL = """
Bonjour %s,

L'équipe de l'AEDI a le plaisir de te proposer le service Taiga.
Taiga est un outil de gestion de projet agile. Il est très bien fait et te seras décisif lors de tes travaux de groupe.
Tu as accès à un compte complet sans aucune limitation qui vaut plus de 100$/mois.
Essaie Taiga dès maintenant et n'hésite pas à nous donner ton avis sur aedi.bureau@listes.insa-lyon.fr

***** Ton compte Taiga *****
  Vas sur https://webaedi.insa-lyon.fr
  Login    : %s
  Password : %s
  (Mot de passe temporaire, merci de le changer rapidement)
******************************

L'inscription publique est fermée. Tu peux cependant inscrire directement tes amis depuis tes projets.

Cordialement,
L'équipe DSI de l'AEDI
"""
