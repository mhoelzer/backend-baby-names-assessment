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
    Given a file name for baby.html, returns a list starting with the year
    string followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    result = []
    with open(filename, "r") as opened_file:
        file_info = opened_file.read()
        year_line = re.search(r"Popularity in (\d{4})", file_info)
        if not year_line:
            print("couldnt extract the year")
            return None
        year_isolated = year_line.group(1)
        result.append(year_isolated)
        name_lines = re.findall(
            r"<td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>", file_info)
        names_data = {}
        for name in name_lines:
            rank_isolated = name[0]
            names_data[name[1]] = rank_isolated
            names_data[name[2]] = rank_isolated
        names_data = sorted(names_data.items())
        for key, value in names_data:
            result.append(key + " " + value)
    return result


def create_parser():
    """Create a cmd line parser object with 2 argument definitions"""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--summaryfile', help='creates a summary file', action='store_true')
    parser.add_argument('files', help='filename(s) to parse', nargs='+')
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    if not args:
        parser.print_usage()
        sys.exit(1)
    file_list = args.files
    create_summary = args.summaryfile
    for filename in file_list:
        data = extract_names(filename)
        textie = "\n".join(data)
        if create_summary:
            with open("{}.summary".format(filename), "w") as output_file:
                output_file.write(textie)
        else:
            print(data)


if __name__ == '__main__':
    main()
