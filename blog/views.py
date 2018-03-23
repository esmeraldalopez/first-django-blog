from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post #incluyo el modelo definido en models, .models indica que buscara en el mismo directorio

# Create your views here.
def post_list(request):
    posts =  Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') #QuerySet
    return render(request, 'blog/post_list.html', {'posts':posts})

#post_detail recibe pk, que es lo que recibira en la url, que bien puede ser el numero de blog, para este caso
def post_detail(request, pk):
    #QuerySet para buscar el post
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
