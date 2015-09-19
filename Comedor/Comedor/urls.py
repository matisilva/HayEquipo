from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^asistencias/', include('Asistencias.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
