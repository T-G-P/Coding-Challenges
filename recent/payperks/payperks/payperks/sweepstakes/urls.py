from django.conf.urls import patterns, url

from sweepstakes import views

urlpatterns = patterns(
    '',
    url(r'^users/points/$', views.earn_points),
    url(r'^users/prize/$', views.check_or_claim_prize),
    url(r'^sweeps/$', views.run_sweeps),
)
