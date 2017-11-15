#!/usr/bin/python
#
# Copyright 2017 Tim Hall

import sys
import pysrt
import os
from os.path import join, getsize
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
    s = s.replace("\n", " ")
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

src_dir = sys.argv[1]

for root, dirs, files in os.walk(src_dir):
    print root, "consumes",
    print sum(getsize(join(root, name)) for name in files),
    print "bytes in", len(files), "non-directory files"
    for d in dirs:
        for filename in d:
            if filename.endswith(".srt"):
                filename_noext = filename[0:-4]
                file_path = os.path.join(src_dir, filename)
                print "Full file path = " + file_path
                subs = pysrt.open(file_path)
                transcript = ""
                for sub in subs:
                    text = sub.text
                    text = clean_sub(text)
                    print "text = " + text
                    transcript += text
                with open(filename_noext + ".csv", 'wb') as csvfile:
                    filewriter = csv.writer(csvfile, delimiter=',',
                                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    filewriter.writerow(['Name', 'Front', 'Back'])
                    filewriter.writerow([filename_noext, filename_noext, transcript])
                continue
            else:
                continue






# print "srt_file = " + str(srt_file)
# print ""
# print "transcript = " + transcript
# print ""
# print "subs = " + str(subs)
print "Current working dir : %s" % os.getcwd()
print "os.path.dirname... is %s" % os.path.dirname(os.path.realpath(sys.argv[0]))
print "Script Finished."


