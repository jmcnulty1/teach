from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',        'main.views.home',   name='home'),
    url(r'^tomato/$', 'main.views.tomato', name='home2'),
    #url(r'^pizza/$',  'main.views.away', name='away'),
    # url(r'^$', 'bigidea.views.home', name='home'),
    # url(r'^bigidea/', include('bigidea.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
