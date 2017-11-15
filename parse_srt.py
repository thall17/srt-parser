#!/usr/bin/python
#
# Copyright 2017 Tim Hall

import sys
import pysrt
import os

# Helper functions


def clean_sub(s):
    s = remove_carats(s)
    s = add_spacing(s)

    return s

def add_spacing(s):
    new_string = s
    new_string += " "
    return new_string


def remove_carats(s):
    if s[0:2] == ">>":
        new_string = s[2:-1]
    else:
        new_string = s
    return new_string


# args must be 2 or 3 params long [script_name, src_dir, dest_dir]
if (len(sys.argv) < 2) or (len(sys.argv) > 3):
    print "Wrong # of parameters."
    print "Syntax:    'python parse_srt.py <src_dir> [dest_dir]'"
    print "<src_dir> is required and should contain .srt files, or contain folders which each contain .srt files."
    print "[dest_dir] is optional, and will default to src_dir if not provided"
    exit()

srt_file = sys.argv[1]
subs = pysrt.open(srt_file)

transcript = ""

for sub in subs:
    text = sub.text
    text = clean_sub(text)
    print "text = " + text
    transcript += text

print "srt_file = " + str(srt_file)
print ""
print "transcript = " + transcript
print ""
print "subs = " + str(subs)
print "Current working dir : %s" % os.getcwd()
print "os.path.dirname... is %s" % os.path.dirname(os.path.realpath(sys.argv[0]))
print 'Script Finished'



