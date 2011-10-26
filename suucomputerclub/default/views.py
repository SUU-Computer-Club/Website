from django.shortcuts import render_to_response
from django.template import RequestContext
# Create your views here.

def index(request):
    return render_to_response('base.html', locals(), context_instance=RequestContext(request))
