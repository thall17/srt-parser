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

if not os.path.exists(src_dir + "/output"):
    os.makedirs(src_dir + "/output")

if not os.path.exists(src_dir + "/output/html"):
    os.makedirs(src_dir + "/output/html")

if not os.path.exists(src_dir + "/output/csv"):
    os.makedirs(src_dir + "/output/csv")

for root, dirs, files in os.walk(src_dir):
    print root, "consumes",
    print sum(getsize(join(root, name)) for name in files),
    print "bytes in", len(files), "non-directory files"

    # Iterate directories within root directory:
    for d in dirs:
        if d != "output":

            print"d name is " + d
            full_directory = src_dir + "/" + d + "/"

            # Create .rtf files:
            f = open(src_dir + "/output/html/" + d + ".html", 'wb')
            f.write("<h1>" + d + "</h1>")
            f.write("<ul>")
            f.write("<li>Hello World</li>")
            f.write("<ul>")
            f.write("<li>Hello World again (subbullet)!</li>")
            f.write("</ul>")
            f.write("</ul>")
            f.close()
            # Create csv file named after the current directory:
            with open(src_dir + "/output/csv/" + d + ".csv", 'wb') as csvfile:
                filewriter = csv.writer(csvfile, delimiter=',',
                                        quotechar='"', quoting=csv.QUOTE_MINIMAL)
                filewriter.writerow(['Name', 'Question', 'Answer'])

                # Add a row to the csv for every video
                for filename in os.listdir(src_dir + "/" + d + "/"):
                    full_filename = full_directory + filename
                    print "filename is " + filename
                    if filename.endswith(".srt"):
                        filename_noext = filename[0:-4]
                        subs = pysrt.open(full_filename)
                        transcript = ""
                        for sub in subs:
                            text = sub.text
                            text = clean_sub(text)
                            print "text = " + text
                            transcript += text
                        filewriter.writerow([filename_noext, filename_noext, transcript])
                        continue
                    else:
                        continue

# print "srt_file = " + str(srt_file)
# print ""
# print "transcript = " + transcript
# print ""
# print "subs = " + str(subs)
# print "Current working dir : %s" % os.getcwd()
# print "os.path.dirname... is %s" % os.path.dirname(os.path.realpath(sys.argv[0]))
print "Script Finished."


