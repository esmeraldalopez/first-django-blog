from django.shortcuts import render
from django.utils import timezone
from .models import Post #incluyo el modelo definido en models, .models indica que buscara en el mismo directorio

# Create your views here.
def post_list(request):
    posts =  Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') #QuerySet
    return render(request, 'blog/post_list.html', {'posts':posts})
