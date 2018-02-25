from django.db import models
from django.utils import timezone
#from e import añaden algo de otros archivos, entonces en vez de copiar
#y pegar las mismas cosas en cada archivo podemos incluirlas de esta manera

class Post(models.Model): #definicion del modelo Post (OBJETO)
    #modesl.Model indica que Post es un modelo de Django, entonces Django
    #sabe que debe guardarlo en la BD
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) #vinculo con otro modelo
    title = models.CharField(max_length=200) #con models.CharField es como se define un texto con un num. limitado de caracteres -titulo del post
    text = models.TextField() #este es para textos largos...sin limite -texto del post
    created_date = models.DateTimeField(
            default=timezone.now) #fecha y hora
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self): #metodo publish; def indica que es una funcion o un metodo
        self.published_date = timezone.now()
        self.save()

    def __str__(self): #metodo de retorno, cuando lo llamemos unos devolvera el string del titulo del post; esta linea lleva "dunder" (double-underscore)
        return self.title
