
#############################################################
#                                                           #
# scrape - a webpage scraping tool                          #
# written by Hunter Hammond (huntrar@gmail.com)             #
#                                                           #
#############################################################


import argparse
import sys
from urlparse import urlparse

from utils import *
from . import __version__

import lxml.html as lh
import pdfkit as pk


def get_parser():
    parser = argparse.ArgumentParser(description='a webpage scraping tool')
    parser.add_argument('url', type=str, help='url to scrape')
    parser.add_argument('keywords', type=str, nargs='*', 
                        help='keywords to search')
    parser.add_argument('-c', '--crawl', type=str, nargs='*',
                        help='crawl links based on these keywords')
    parser.add_argument('-ca', '--crawl-all', help='crawl all links',
                        action='store_true')
    parser.add_argument('-l', '--limit', type=int, help='crawl page limit')
    parser.add_argument('-t', '--text', help='write to text instead of pdf',
                        action='store_true')
    parser.add_argument('-v', '--version', help='display current version',
                        action='store_true')
    return parser

def crawl(args, url):
    try:
        links = set(get_html(url).xpath('//a/@href'))
    except TypeError:
        return None

    search_words = args['crawl']
    if search_words:
        filtered_links = []
        for link in links:
            for word in search_words:
                if word in link:
                    filtered_links.append(link)
                    break
    else:
        filtered_links = list(links)

    filtered_links.insert(0, url)
    filtered_links = filter(validate_url, filtered_links)
    return filtered_links

def write_pages(args, links, filename):
    if args['text']: 
        filename = filename + '.txt'
        print('Writing {} page(s) to {}'.format(len(links), filename))

        print_pg_num = len(links) > 1

        for i, link in enumerate(links):
            html = get_html(link)

            if html is not None:
                text = get_text(html, args['keywords'])
                with open(filename, 'a') as f:
                    if print_pg_num:
                        f.write('\n\n')
                        f.write('~~~ Page {} ~~~\n'.format(str(i+1)))
                    for line in text:
                        f.write(line)
            else:
                sys.stderr.write('Failed to parse {}.\n'.format(link))
    else:
        filename = filename + '.pdf'
        print('Writing {} page(s) to {}'.format(len(links), filename))
        pk.from_url(links, filename)

def scrape(args):
    url = clean_url(args['url'])
    base_url = '{url.netloc}'.format(url=urlparse(url))
    
    for b in base_url.split('.'):
        if len(b) > 3:
            base_url = b
            break

    filename = base_url + '-' + url.strip('/').split('/')[-1]

    if args['crawl'] or args['crawl_all']:
        links = crawl(args, url)
    else:
        links = [url]
    
    if args['limit']:
        limit = args['limit']
    else:
        limit = len(links)
    write_pages(args, links[:limit], filename)

def command_line_runner():
    parser = get_parser()
    args = vars(parser.parse_args()) 

    if args['version']:
        print(__version__)
        return

    if not args['url']:
        parser.print_help()
    else:
        scrape(args)

if __name__ == '__main__':
    command_line_runner()
