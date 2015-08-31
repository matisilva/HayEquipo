from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.Home.as_view(), name='home'),
    url(r'^(?P<pk>[0-9]+)/$', views.QuestionDetailView.as_view(), name='detail'),
]


