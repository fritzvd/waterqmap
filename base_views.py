from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.views.generic.simple import direct_to_template
from django.contrib.auth import authenticate, login
from django.template import RequestContext

def home_page(request):
    return direct_to_template(request, 'home.html')
