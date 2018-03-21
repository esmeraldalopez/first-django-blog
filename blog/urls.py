from django.conf.urls import include, url #importamos los metodos de Django
from . import views #importamos todas nuestras views

#primer patron URL
urlpatterns = [
    url(r'^$', views.post_list),  #asignamos una view llamada post_list al url '^$'
]
