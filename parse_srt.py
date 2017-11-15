#!/usr/bin/python
#
# Copyright 2017 Tim Hall

import sys
import pysrt
import os
import csv

# args must be 2 or 3 params long [script_name, src_dir, dest_dir]
if (len(sys.argv) < 2) or (len(sys.argv) > 3):
    print "Wrong # of parameters."
    print "Syntax:    'python parse_srt.py <src_dir> [dest_dir]'"
    print "<src_dir> is required and should contain .srt files, or contain folders which each contain .srt files."
    print "[dest_dir] is optional, and will default to src_dir if not provided"
    exit()

# Helper functions
def clean_sub(s):
    s = s.rstrip()
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

srt_file = sys.argv[1]
file_name = srt_file[0:-4]
subs = pysrt.open(srt_file)

transcript = ""

for sub in subs:
    text = sub.text
    text = clean_sub(text)
    print "text = " + text
    transcript += text

# transcript = transcript.rstrip()
transcript = transcript.replace(",", ";")
# transcript = "|" + transcript + "|"



with open('Test.csv', 'wb') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Name', 'Profession', 'Answer'])
    filewriter.writerow([file_name, file_name, transcript])


print "srt_file = " + str(srt_file)
print ""
print "transcript = " + transcript
print ""
print "subs = " + str(subs)
print "Current working dir : %s" % os.getcwd()
print "os.path.dirname... is %s" % os.path.dirname(os.path.realpath(sys.argv[0]))
print ""
print "subs[0].text = " + subs[0].text.rstrip()
print 'Script Finished'



