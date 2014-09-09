from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'acra_django_server.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^dashboard/', 'acra.views.dashboard', name='dashboard'),
    
    url(r'^timeline/', 'acra.views.timeline', name='timeline'),
    url(r'^acra/', include("acra.urls")),
    url(r'^acra-vivintsky/', include("acra.urls")),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    
    url(r'^$', 'acra.views.dashboard', name='dashboard'),

)
