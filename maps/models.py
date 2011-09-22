from django.db import models

class Map(models.Model):
    title = models.CharField(max_length=70)
    slug = models.SlugField()
    url = models.URLField()
    def __unicode__(self):
        return self.title

class MapDate(models.Model):
    spec_map = models.ForeignKey(Map)
    date = models.DateField()
