from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from flowik.views import GetAuthenticatedUser
from flows.handler import FlowHandler
handler = FlowHandler()
handler.register_entry_point(GetAuthenticatedUser)


urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'selfhelp.views.home', name='home'),
    #url(r'^selfhelp/', include('selfhelp.foo.urls')),
    #url(r'^start/', 'flowik.views.simpleview', name='simple'),
    url(r'^start/(?P<step_id>\d+)/$', 'dbflow.views.step_display', name='step'),
    url(r'^start/$', 'dbflow.views.step_display', name='step'),
    url(r'^post_redirect/$', 'dbflow.views.post_redirect', name='post'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': '/home/vmplanet/selfhelp/dbflow/static'}),
)

#urlpatterns = handler.urls
