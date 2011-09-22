from maps.models import Map
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.core import serializers

def map_view(request, map_id):
    d = get_object_or_404(Map, pk=map_id)
    return render_to_response('maps/maps.html', {'map':d})

def json_dates(request, map_id):
    d = get_object_or_404(Map, pk=map_id)
    daties = d.mapdate_set.all()
    datie = daties.values()
    return render_to_response('maps/dates.js', {'date':datie}, mimetype='text/javascript')
#    return HttpResponse(serializers.serialize('json', daties, fields=('date')), mimetype='application/json')
