from django.conf.urls.defaults import patterns, url

from views import AdhesionFormView

urlpatterns = patterns('members.views',
    url(r'^adhesion/demande/$', AdhesionFormView.as_view(), name="adherer"),
    url(r'^adhesion/demande/confirm/$', 'adherer', name="adherer_post"),
)
