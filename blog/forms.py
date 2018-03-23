from django import forms
from .models import Post

#PostForm es el nombre del formulario
class PostForm(forms.ModelForm): #entre parentesis se indica a Django que PostForm es un formulario

    class Meta: #aqui indicamos que modelo va a utilizar para crear el formulario
        model = Post
        fields = ('title', 'text',) #indicamos los campos que queremos en el formulario
