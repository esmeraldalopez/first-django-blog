from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)), #url del admin
    url(r'', include('blog.urls')), #aqui solo incluimos o importamos nuestro archivo en blog.urls para dejar este 'limpio'
]
