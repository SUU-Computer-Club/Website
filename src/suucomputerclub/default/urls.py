from django.conf.urls.defaults import url, patterns, include

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('default.views',
    url(r'^$', 'index', name='index'),
    url(r'^calendar/$', 'calendar', name='calendar'),
    url(r'^projects/$', 'projects', name='projects'),
    url(r'^constitution/$', 'constitution', name='constitution'),
    url(r'^faq/$', 'faq', name='faq'),
    url(r'^about/$', 'about', name='about'),
)
