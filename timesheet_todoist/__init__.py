#!/usr/bin/env python

import mytime
import datetime
import sys
import re
import argparse
import parsedatetime as pdt
from os.path import expanduser
import os

def read_rc_value(file, key):
    filevalue = ""
    filekey = ""
    if file == "":
        file = expanduser("~") + "/.todoistprodrc"

    # Check to see if file exists
    if os.path.exists(file):
        # ASSERT: file exists
        f=open(file, 'r')
        content = f.readlines()
        for line in content:
            matchObj = re.match('^#.*', line, re.M|re.I)
            if matchObj:
                pass
            else:
                matchObj = re.match('^\n$', line, re.M|re.I)
                if matchObj:
                    pass
                else:
                    filekey, value = line.rstrip('\n').split('=')
                    if (filekey == key):
                        filevalue = value
                        break

        f.close()
        if (filekey == ""):
            print "Could not find key '" + key + "' in " + file
            sys.exit()

        if (filevalue == ""):
            print "Could not find a value for '" + key + "' in " + file
            sys.exit()

        return filevalue

    else:
        # ASSERT: file does not exists
        print "Could not find run control file: .todoistprodrc"
        sys.exit()

def get_ptn_by_date(file, date, tag):
    ptn = ""
    f=open(file, 'r')
    for lines in f.readlines():
        fields = lines.rstrip('\n').split('|')
        if fields[0] == tag:
            ptn = parse_ptn_by_date(fields, date)
            break

    f.close()
    return ptn

def parse_ptn_by_date(fields, date):
    ptn = ""
    ptn_list = fields[1].split(';')
    for p in ptn_list:
        start_date, end_date, ptn = p.split(',')
        dt_start = int(datetime.datetime.strptime(start_date, "%Y-%m-%d").strftime('%s'))
        dt_end = int(datetime.datetime.strptime(end_date, "%Y-%m-%d").strftime('%s'))
        dt_date = int(datetime.datetime.strptime(date, "%Y-%m-%d").strftime('%s'))
        if dt_date >= dt_start and dt_date <= dt_end:
            break

    return ptn
