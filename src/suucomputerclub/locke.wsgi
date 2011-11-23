import os, sys
sys.path.append('/var/django/locke/src/')
sys.path.append('/var/django/locke/src/computerclub/')
#sys.path.append('/usr/local/lib/python2.6/dist-packages/django_haystack-1.2.5-py2.6.egg/haystack/backends')
# may be required :)
#sys.path.append('/path/to/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'suucomputerclub.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
