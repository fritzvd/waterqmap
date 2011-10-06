from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=70)
    def __unicode__(self):
        return self.title

class Map(models.Model):
    title = models.CharField(max_length=70)
    url = models.URLField()
    def __unicode__(self):
        return self.title

class MapDate(models.Model):
    spec_map = models.ForeignKey(Map)
    date = models.DateField(unique=True)
