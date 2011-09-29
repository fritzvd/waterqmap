from waterqmap.maps.models import Map,MapDate
from django.contrib import admin

class MapDateInline(admin.TabularInline):
    model = MapDate

class MapAdmin(admin.ModelAdmin):
    prepopulated_field = {"slug": ("title",)}
    inlines = [MapDateInline]


admin.site.register(Map, MapAdmin)
