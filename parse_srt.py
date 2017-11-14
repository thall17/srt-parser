#!/usr/bin/python
#
# Copyright 2017 Tim Hall


import sys
import pysrt

if len(sys.argv) != 2:
    print "Syntax:"
    print "    python parse_srt.py <directory_containing_srt_files>"
    exit()