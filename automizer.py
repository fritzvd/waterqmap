#!/usr/bin/python
import os, sys, datetime, subprocess
from fileinput import input
from maps.models import Map
import settings

mapfile = '/home/fritz/WebDev/algae2010.map'
txt = '/home/fritz/WebDev/layers.txt'

def get_date_mapfile(mapfile, txt):
    print "getting mapfile, writing dates to txtfile"
    readdates = """grep -E "NAME" """ + mapfile + """ | sed -e 's/[^0-9]//g' -e '/^$/ d' > """ + txt
    subprocess.call(readdates, shell=True)

def read_write_dates():
    rtxt = open(txt)
    print "reading text file saving dates as datetime objects"
    read_it = rtxt.readlines()
    del read_it[0:1]
    maps = []
    map_ = Map.objects.filter(url__endswith="2011.map")[1]
    for lines in read_it:
        line = lines.strip()
        month = int(line[0:2])
        day = int(line[2:4])
        datum = datetime.date(2011, month, day)
        map_.mapdate_set.get_or_create(date=datum)

get_date_mapfile(mapfile, txt)
read_write_dates()

