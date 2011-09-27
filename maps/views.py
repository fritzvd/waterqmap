from maps.models import Map
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.core import serializers
from django.contrib.auth import authenticate, login

def map_view(request, map_id):
    d = get_object_or_404(Map, pk=map_id)
    if request.user.is_authenticated():
        d = get_object_or_404(Map, pk=map_id)
    else:
        d = 'bummernotloggedin'
    return render_to_response('maps/maps.html', {'map':d})

def json_dates(request, map_id):
    d = get_object_or_404(Map, pk=map_id)
    daties = d.mapdate_set.all()
    datie = daties.values()
    if request.user.is_authenticated():
        return render_to_response('maps/dates.js', {'date':datie}, mimetype='text/javascript')
    else:
        return HttpResponse('You are not logged in and as a consequence do not have access to this information')
        #    return HttpResponse(serializers.serialize('json', daties, fields=('date')), mimetype='application/json')
