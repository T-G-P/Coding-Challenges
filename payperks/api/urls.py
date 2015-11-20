from django.conf.urls import patterns, url, include

from .views import UserSweeps, UserDetail

user_urls = patterns('',
    url(r'^/(?P<username>[0-9a-zA-Z_-]+)/sweeps$', UserPostList.as_view(), name='user-sweeps'),
    url(r'^/(?P<username>[0-9a-zA-Z_-]+)$', UserDetail.as_view(), name='user-detail'),
)

urlpatterns = patterns('',
    url(r'^users', include(user_urls)),
)
