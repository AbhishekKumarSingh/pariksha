from django.conf.urls import patterns, url
from quiz import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/detail/$', views.QuestionDetailView.as_view(), name='detail'),
    url(r'^result/', views.ResultView.as_view(), name='result'),
    url(r'^response/(?P<pk>\d+)/$', views.UserResponseView.as_view(),
        name='response'),
    url(r'^(?P<pk>\d+)/next/', views.next_view, name='next'),
    url(r'^(?P<pk>\d+)/qdetail', views.QuizHomeView.as_view(),
        name='quiz_detail'),
    #url(r'^(?P<pk>\d+)/qdetail', views.QuizDetailView.as_view(),
    # name='quiz_detail'),
)
