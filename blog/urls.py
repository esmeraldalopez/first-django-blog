from django.conf.urls import include, url #importamos los metodos de Django
from . import views #importamos todas nuestras views

#primer patron URL
urlpatterns = [
    url(r'^$', views.post_list),  #asignamos una view llamada post_list al url '^$'
           #/post/12345678904521/ el numero es = pk
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    #?P<pk>[0-9]+) Django llevara todo lo que coloque aqui y lo tranferirá a una vista como una variable llamada pk que es la abreviacion de Primary Key, que se utiliza a menudo en proyectos de Django pero podemos llamarlo como gustemos ej: post_id
     #0-9 dice que solo puede ser un numero, NO una letra
     #significa que debe uno o mas digitos, ES DECIR
     #http://127.0.0.1:8000/post// no es correcto
     #http://127.0.0.1:8000/post/1234567890/ SI ES CORRECTO
    url(r'^post/new/$', views.post_new, name='post_new'),

    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]
#URL para el view post_detail http://127.0.0.1:8000/post/1/
