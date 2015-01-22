from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
        url(r'^$', views.IndexView.as_view(), name='index'),
        url(r'^(?P<pk>\d+)/', views.DetailView.as_view(), name='details'),
        url(r'^results/(?P<pk>\d+)/$', views.ResultView.as_view(), name='results'),
        url(r'^vote/(?P<poll_id>\d+)$', views.vote, name='vote'),
    )
