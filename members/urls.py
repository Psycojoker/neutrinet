from django.conf.urls.defaults import patterns, url
from django.views.generic import ListView
from django.contrib.auth.decorators import user_passes_test

from models import Member
from views import AdhesionFormView

urlpatterns = patterns('members.views',
    url(r'^adhesion/demande/$', AdhesionFormView.as_view(), name="adherer"),
    url(r'^adhesion/demande/confirm/$', 'adherer', name="adherer_post"),
    url(r'^adhesion/list/$', user_passes_test(lambda u: u.is_superuser, "/admin/")(ListView.as_view(queryset=Member.objects.filter(demande__isnull=False))), name="adherer_list"),
)
