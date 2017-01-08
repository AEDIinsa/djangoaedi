from django.dispatch import receiver
import django_cas_ng.signals
from django.contrib.auth.models import User, Group

@receiver(django_cas_ng.signals.cas_user_authenticated) 
def handler_login(sender, **kwargs): 
    attributes = kwargs['attributes']

    promo = attributes['supannEtuInscription'].split('][')
    promo[0] = promo[0][1:]
    promo[-1] = promo[-1][0:-1]
    promo_dict = dict(x.split('=') for x in promo)
    try:
        group = Group.objects.get(name=promo_dict['affect'])
    except Group.DoesNotExist:
        group = Group.objects.create(name=promo_dict['affect'])

    student = User.objects.get(username=kwargs['user'])
    if kwargs['created']:
        student.email = attributes['mail']
        student.first_name=attributes['givenName']
        student.last_name=attributes['sn']
        student.groups.set([group])
        student.save()
