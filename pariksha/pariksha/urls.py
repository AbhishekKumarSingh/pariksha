from django.conf.urls import patterns, include, url
from django.contrib import admin
from views import SignupView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pariksha.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^accounts/register/', SignupView.as_view(), name='signup'),
    url(r'^quiz/', include('quiz.urls', namespace='quiz')),
    url(r'^admin/', include(admin.site.urls)),
)
