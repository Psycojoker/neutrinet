from django.conf.urls.defaults import patterns, url

from views import AdhesionFormView

urlpatterns = patterns('members.views',
    url(r'^adherer/$', AdhesionFormView.as_view(), name="adherer"),
    url(r'^adherer/post/$', 'adherer', name="adherer_post"),
)
