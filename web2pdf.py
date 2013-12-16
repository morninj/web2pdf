#!/usr/bin/env python
from subprocess import call
import argparse
import sys
import os

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--url', help='The URL of a single page ' \
    + 'to download.')
parser.add_argument('-f', '--filename', help='The name of a file containing ' \
    + 'multiple URLs to download. Put each URL on a new line.')
parser.add_argument('-o', '--output', help='If you\'re archiving just one ' \
    + 'page, this is the name of the output file. The default is ' \
    + 'archive.pdf.')
parser.add_argument('-d', '--directory', help='The name of the directory ' \
    + 'to store multiple archives. The default is "archives."')
args = parser.parse_args()

def web2pdf():
    if args.url and not args.filename:
        # Save a single URL
        output_filename = 'archive.pdf'
        if args.output: output_filename = args.output
        make_screenshot(args.url, output_filename)
    elif args.filename and not args.url:
        # Save multiple URLs
        # Create the archives directory
        archives_directory = 'archives'
        if args.directory: archives_directory = args.directory
        call(['mkdir', archives_directory])
        # Process each line in the input file
        with open(args.filename) as f:
            counter = 0
            for line in f:
                print 'Archiving %s...' % line.strip()
                # Generate filenames: 01.pdf, 02.pdf, ..., 99.pdf
                counter = counter + 1
                output_filename = str(counter)
                if counter < 10: output_filename = '0' + output_filename
                output_filename = archives_directory + '/' \
                    + output_filename + '.pdf'
                make_screenshot(line.strip(), output_filename)
    else:
        # No URL or list of URLs provided
        print 'Please give either a URL or a filename containing a list of URLs.'
        sys.exit()
    print 'Done.'

def make_screenshot(url, filename):
    # Call PhantomJS and suppress its output
    with open(os.devnull, "w") as fnull: 
        call(
            ['phantomjs', 'screenshot.js', url, filename],
            stdout=fnull,
            stderr=fnull
        )

if __name__ == '__main__':
    web2pdf()
