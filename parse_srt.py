#!/usr/bin/python
#
# Copyright 2017 Tim Hall


import sys
import pysrt
import os

if not 1 < len(sys.argv) < 4:
    print "Wrong # of parameters."
    print "Syntax:    'python parse_srt.py <src_dir> [dest_dir]'"
    print "<src_dir> is required and should contain .srt files, or contain folders which each contain .srt files."
    print "[dest_dir] is optional, and will default to src_dir if not provided"
    exit()

# subs = pysrt.open('some/file.srt')

print "Current working dir : %s" % os.getcwd()
print "os.path.dirname... is %s" % os.path.dirname(os.path.realpath(sys.argv[0]))
print 'Script Finished'