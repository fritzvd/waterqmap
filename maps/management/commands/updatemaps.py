from django.core.management.base import NoArgsCommand

class Command(NoArgsCommand):
    help = "Update the dates of the maps that are in the database for the datepicker"
    def handle_noargs(self, **options):
        import urllib2, datetime, os
        from xml.dom.minidom import parse
        from maps.models import Map
        print "Go through all Map objects"
        maps = Map.objects.all()
        print "Find the url for every map and parse its GetCapabilities xml request"
        for singlemap in maps:
            document = parse(urllib2.urlopen(singlemap.url + '&request=GetCapabilities&service=WMS'))
            layers = document.getElementsByTagName("Layer")
            # skip last layer, copyright layer
            layers.pop()
            print "Finding and inserting dates for " + singlemap.title + " map"
            for layer in layers:
                if layer.childNodes[5]:
                    title = layer.childNodes[5]
                    if layer.childNodes:
                        datestring = title.childNodes[0].nodeValue
                        if datestring.isdigit():
                            month = int(datestring[0:2])
                            day = int(datestring[2:4])
                            date = datetime.date(2011, month, day)
                            singlemap.mapdate_set.get_or_create(date=date)
