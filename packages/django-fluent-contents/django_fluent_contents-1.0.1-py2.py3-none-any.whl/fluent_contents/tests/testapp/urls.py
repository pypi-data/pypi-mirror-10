from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    #url(r'^comments/', include('django.contrib.comments.urls')),
    #url(r'^forms/', include('form_designer.urls')),
)
