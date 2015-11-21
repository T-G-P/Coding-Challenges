from django.conf.urls import patterns, url, include

from sweepstakes import views

user_urls = patterns(
    '',
    url(r'^users/(?P<id>[0-9]+)/points$', views.earn_points),
    url(r'^users/(?P<id>[0-9]+)/sweeps$', views.run_sweeps),
    url(r'^users/(?P<id>[0-9]+)/drawings/(?P<id>[0-9]+)$', views.check_prize),
    url(r'^users/(?P<id>[0-9]+)/drawings/(?P<id>[0-9]+)$', views.claim_prize),
)

urlpatterns = patterns(
    '',
    url(r'^users', include(user_urls)),
)
