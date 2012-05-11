from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('members.urls', namespace='members', app_name='members')),
    url(r'^todo/', include('todo.urls')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^news/', include('basic.blog.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^tweets/', 'views.tweets', name='tweets'),
)
