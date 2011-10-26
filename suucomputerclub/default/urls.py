from django.conf.urls.defaults import url, patterns, include

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('default.views',
    url(r'^$', 'index', name='index'),
)
