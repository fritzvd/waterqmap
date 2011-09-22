#!/usr/bin/python
import os, sys, datetime, subprocess
from fileinput import input
from maps.models import Map

mapfile = '/home/fritz/WebDev/algae2011.map'
txt = '/home/fritz/WebDev/layers.txt'
js = '/home/fritz/WebDev/datepick/js/enabledates.js'

def get_date_mapfile(mapfile, txt):
    print "getting mapfile, writing dates to txtfile"
    readdates = """grep -E "NAME" """ + mapfile + """ | sed -e 's/[^0-9]//g' -e '/^$/ d' > """ + txt
    subprocess.call(readdates, shell=True)

rtxt = open(txt)
wjs = open(js, "w")
maps = []

def read_write_dates():
    print "reading text file saving dates as datetime objects"
    read_it = rtxt.readlines()
    del read_it[0:1]
    for lines in read_it:
        line = lines.strip()
        year = int(line[0:4])
        month = int(line[4:6])
        day = int(line[6:8])
        datum = datetime.date(year, month, day)
        maps.append(datum)
    for i in range(len(maps)):
        

get_date_mapfile(mapfile, txt)
read_write_dates()

