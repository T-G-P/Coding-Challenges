from django.conf.urls import patterns, url, include

from sweepstakes import views

user_urls = patterns(
    '',
    url(r'^users/points/$', views.earn_points),
    url(r'^users/sweeps/$', views.run_sweeps),
    url(r'^users/prize/$', views.check_prize),
    url(r'^users/prize/$', views.claim_prize),
)

urlpatterns = patterns(
    '',
    url(r'^users', include(user_urls)),
)
