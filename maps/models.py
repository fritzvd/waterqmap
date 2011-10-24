from django.db import models

class Map(models.Model):
    title = models.CharField(max_length=70)
    url = models.URLField()
    minx = models.FloatField()
    miny = models.FloatField()
    maxx = models.FloatField()
    maxy = models.FloatField()
    def __unicode__(self):
        return self.title

class MapDate(models.Model):
    map = models.ForeignKey(Map)
    date = models.DateField()
