from django.conf.urls import url

from . import views

app_name='aedisite'
urlpatterns = [
    url(r'^$', views.render_static, {'filename': 'index.html'}, name='index'),
    url(r'^presentation/$', views.render_static, {'filename': 'presentation.html'}, name='presentation'),
    url(r'^etudiant/agenda/$', views.render_static, {'filename': 'agenda_etudiant.html'}, name='agenda'),
    url(r'^etudiant/services/$', views.render_static, {'filename': 'services.html'}, name='services'),
    url(r'^entreprise/rencontresif/$', views.render_static, {'filename': 'rencontresif.html'}, name='rencontresif'),
    url(r'^entreprise/entretiens/$', views.render_static, {'filename': 'entretiens.html'}, name='entretiens'),
    url(r'^entreprise/conferences/$', views.render_static, {'filename': 'conferences.html'}, name='conferences'),
    url(r'^entreprise/parrain/$', views.render_static, {'filename': 'parrain.html'}, name='parrain'),
    url(r'^contact/$', views.render_static, {'filename': 'contact.html'}, name='contact'),
]
