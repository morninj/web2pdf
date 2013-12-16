# web2pdf

Convert webpages to PDFs for offline reading.

## Installation

First,  [install PhantomJS](http://phantomjs.org/download.html).

Second, clone this repository:

    $ git clone https://github.com/morninj/web2pdf.git

## Use

### Add web2pdf to Your Path

    $ cp web2pdf.py /usr/local/bin/web2pdf
    $ chmod +x /usr/local/bin/web2pdf

### Archive a Single URL

    $ web2pdf -u http://www.nytimes.com/

This will save the page as `archive.pdf`. You can change the default filename:

    $ web2pdf -u http://www.nytimes.com/ -o nytimes.pdf

### Archive Multiple URLs

Create a file named `input.txt` (or anything else) with one URL per line, like 
this:

    http://www.nytimes.com/
    http://news.ycombinator.com/
    http://www.reddit.com/

Then, run:

    $ web2pdf -f input.txt

This will save each page in a new folder named `archives`. You can also change 
the name of the folder:

    $ web2pdf.py -f input.txt -d my_folder

