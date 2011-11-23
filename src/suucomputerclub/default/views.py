from django.shortcuts import render_to_response, RequestContext
from suucomputerclub import slides
'''
The homepage, not only that but it includes a function
for a slideshow. The slideshow automatically reads any
directories in the SLIDESHOW_PATH. If it finds images
in these directories it stores their name, and an
assumed thumbnail location of thumb/[imagename].ext
in the same directory.
'''
def index(request):
    images = slides.get_slides() # See slides.py
    
    ctx = {
        'images': images,
    }
    
    return render_to_response('index.html', ctx, context_instance=RequestContext(request))

def calendar(request):
    return render_to_response('calendar.html', context_instance=RequestContext(request))

def projects(request):
    return render_to_response('projects.html', context_instance=RequestContext(request))

def constitution(request):
    return render_to_response('constitution.html', context_instance=RequestContext(request))

def faq(request):
    return render_to_response('faq.html', context_instance=RequestContext(request))

def about(request):
    return render_to_response('about.html', context_instance=RequestContext(request))