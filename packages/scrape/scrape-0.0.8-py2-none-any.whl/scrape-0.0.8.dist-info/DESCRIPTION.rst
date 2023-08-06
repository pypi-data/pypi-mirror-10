# scrape

## 
a web scraping tool

## Installation
* `pip install scrape`

## Usage
    usage: scrape [-h] [-f [FILTER [FILTER ...]]] [-c [CRAWL [CRAWL ...]]] [-ca]
                  [-l LIMIT] [-t] [-vb] [-v]
                  [urls [urls ...]]

    a web scraping tool

    positional arguments:
      urls                  urls to scrape

    optional arguments:
      -h, --help            show this help message and exit
      -f [FILTER [FILTER ...]], --filter [FILTER [FILTER ...]]
                            filter lines by keywords, text only
      -c [CRAWL [CRAWL ...]], --crawl [CRAWL [CRAWL ...]]
                            enter keywords to crawl links
      -ca, --crawl-all      crawl all links
      -l LIMIT, --limit LIMIT
                            crawl page limit
      -t, --text            write to text instead of pdf
      -vb, --verbose        show pdfkit errors
      -v, --version         display current version

## Author
* Hunter Hammond (huntrar@gmail.com)

## Notes
* Unless specified using the --text flag, all webpages are saved as pdf files using pdfkit.

* The --filter flag may be used in conjunction with --text to only save lines matching one or more keywords provided

* Subsequent links may be followed by entering --crawl-all or --crawl. --crawl accepts a list of substrings to control which URL's to crawl, while --crawl-all will attempt to follow links indefinitely.

* There is no limit to the number of pages to be crawled unless one is set using the --limit flag, thus to cancel crawling and begin processing simply press Ctrl-C.



News
====

0.0.8
------

 - better implementation of crawler, can now scrape entire websites
 - added OrderedSet class to utils.py

0.0.7
------

 - changed --keywords to --filter and positional arg url to urls

0.0.6
------

 - use --keywords flag for filtering text
 - can pass multiple links now
 - will not write empty files anymore

0.0.5
------

 - added --verbose argument for use with pdfkit
 - improved output file name processing

0.0.4
------

 - accepts 0 or 1 url's, allowing a call with just --version

0.0.3
------

 - Moved utils.py to scrape/

0.0.2
------

 - First entry




