#!/usr/bin/python
#
# Copyright 2017 Tim Hall


import sys
import pysrt
import os

# args must be 2 or 3 params long [script_name, src_dir, dest_dir]
if (len(sys.argv) < 2) or (len(sys.argv) > 3):
    print "Wrong # of parameters."
    print "Syntax:    'python parse_srt.py <src_dir> [dest_dir]'"
    print "<src_dir> is required and should contain .srt files, or contain folders which each contain .srt files."
    print "[dest_dir] is optional, and will default to src_dir if not provided"
    exit()

srt_file = sys.argv[1]
subs = pysrt.open(srt_file)

print "srt_file = " + str(srt_file)
print "subs = " + str(subs)
print "Current working dir : %s" % os.getcwd()
print "os.path.dirname... is %s" % os.path.dirname(os.path.realpath(sys.argv[0]))
print 'Script Finished'