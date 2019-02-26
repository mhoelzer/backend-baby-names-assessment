#!/usr/bin/env python
# -*- coding: utf-8 -*-

# BabyNames python coding exercise.

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

__author__ = "mhoelzer"


import sys
import re
import argparse

"""
Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    result = []
    with open(filename, "r") as opened_file:
        file_info = opened_file.read()
    # (P.+n )(\d\d\d\d)
    # (Popularity in )(\d\d\d\d)
    # (<.*?>)(P.+n )(\d\d\d\d)(<\/.*?>)
    year_line = re.search(r"Popularity\sin\s(\d\d\d\d)", file_info)
    assert year_line  # better be not none and if not, stop; can add description
    # ^^^ assert statement is used klie a sanity checkpoint to have dude using as debug to see if thins work
    # ^^^ have even for production just in case but basically gets vcommented out when in prod
    # ^^^ not for data validation/inputs for params; just for vheckign to see if therre
    # ^^^ interpreted when in debug only 
    # if not year_line:
    #     print("couldnt extract the year")
    #     return None  # this works on one file at a time, so no forloop to continue
    year_isolated = year_line.group(1)
    print("foudn year: {}".format(year_isolated))
    result.append(year_isolated)
    name_lines = re.findall(
        r"<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>", file_info)
    # print(name_lines)
    names_data = {}
    for rank, boy, girl in name_lines:
        # this gets each as their own thing
        # rank belongs to boy and girl
        if boy not in names_data:
            # if not already in there, add
            names_data[boy] = rank
        if girl not in names_data:
            names_data[girl] = rank
    sorted_names = sorted(names_data.keys())
    # ^^^ list of names, not dict; gets all the keys, whcih are the names
    # for line in name_lines:
    #     rank_isolated = line.group(0)
    #     boys_name_isolated = "{} {}".format(line.group(1), rank_isolated)
    #     girls_name_isolated = "{} {}".format(line.group(2), rank_isolated)
    #     names_data[boys_name_isolated] = rank_isolated
    #     names_data[girls_name_isolated] = rank_isolated
    # return year_isolated + sorted(names_data)
    for name in sorted_names:
        # going through keys
        result.append(name + " " + names_data[name])
    # print(result)
    return result


def create_parser():
    """Create a cmd line parser object with 2 argument definitions"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--summaryfile', help='creates a summary file', action='store_true')
    # The nargs option instructs the parser to expect 1 or more filenames.
    # It will also expand wildcards just like the shell, e.g. 'baby*.html' will work.
    parser.add_argument('files', help='filename(s) to parse', nargs='+')
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    if not args:
        parser.print_usage()
        sys.exit(1)
    file_list = args.files
    # option flag
    create_summary = args.summaryfile
    # For each filename, get the names, then either print the text output
    # or write it to a summary file
    for filename in file_list:
        data = extract_names(filename)
        if create_summary:
            with open("{}.summary".format(filename), "w") as output_file:
                output_file.write(data)
        else:
            print(data)
    # hardcoded for now
    # extract_names("baby1990.html")


if __name__ == '__main__':
    main()
