from django.conf.urls import patterns, url

from login import views

urlpatterns = patterns(
    '',
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', views.logout_page),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^register/$', views.register),
    url(r'^register/success/$', views.register_success),
    url(r'^home/$', views.home),
    url(r'^admin/$', views.admin),
)
