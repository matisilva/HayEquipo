from django.conf.urls import url, include, patterns

from . import views

urlpatterns = [
    # ex /asistencias/
    url(r'^$', views.index, name='index'),
    # ex: /asistencias/5/
    url(r'^(?P<A_id>[0-9]+)/$', views.details, name='details'),
    # ex: /assist/
    url(r'^assist/', views.assist, name='assist')
]
