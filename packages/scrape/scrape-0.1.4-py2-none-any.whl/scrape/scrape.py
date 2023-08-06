#!/usr/bin/env python

#############################################################
#                                                           #
# scrape - a web scraping tool                              #
# written by Hunter Hammond (huntrar@gmail.com)             #
#                                                           #
#############################################################

import argparse
import sys
from urlparse import urlparse

import lxml.html as lh
import pdfkit as pk

import utils
from . import __version__


def get_parser():
    parser = argparse.ArgumentParser(description='a web scraping tool')
    parser.add_argument('urls', type=str, nargs='*',
                        help='urls to scrape')
    parser.add_argument('-c', '--crawl', type=str, nargs='*',
                        help='keywords to crawl links by')
    parser.add_argument('-ca', '--crawl-all', help='crawl all links',
                        action='store_true')
    parser.add_argument('-f', '--filter', type=str, nargs='*', 
                        help='filter lines of text by keywords')
    parser.add_argument('-l', '--limit', type=int, help='set crawl page limit')
    parser.add_argument('-p', '--pdf', help='write to pdf instead of text',
                        action='store_true')
    parser.add_argument('-s', '--restrict', help='restrict domain to that of the seed url',
                        action='store_true')
    parser.add_argument('-v', '--version', help='display current version',
                        action='store_true')
    parser.add_argument('-vb', '--verbose', help='print pdfkit log messages',
                        action='store_true')
    return parser


def crawl(args, url):
    # The limit on number of pages to be crawled
    limit = args['limit']

    # Whether links must share the same domain as the seed url
    restrict = args['restrict']

    # Domain of the seed url
    domain = args['domain']

    uncrawled_links = utils.OrderedSet()
    crawled_links = utils.OrderedSet()

    html = utils.get_html(url)
    if len(html) > 0:
        raw_links = html.xpath('//a/@href')
    else:
        raw_links = []

    ''' Clean the links, filter by domain if necessary, and update sets
        set_domain inserts the domain from the seed url if none is found
        clean_url removes www. and sets the scheme to http://
    '''
    if raw_links:
        links = [utils.clean_url(utils.set_domain(u, domain)) for u in raw_links]

        if restrict:
            links = filter(lambda x: utils.validate_domain(x, domain), links)

        uncrawled_links.update(filter(lambda x: x not in crawled_links, links))

    crawled_links.add(url)
    print('Crawled {} (#{}).'.format(url, len(crawled_links)))
    
    try:
        while uncrawled_links and (not limit or len(crawled_links) < limit):
            url = uncrawled_links.pop(last=False)

            if utils.validate_url(url):
                html = utils.get_html(url)
                if len(html) > 0:
                    raw_links = html.xpath('//a/@href')
                else:
                    raw_links = []

                ''' Clean the links, filter by domain if necessary, and update sets
                    set_domain inserts the domain from the seed url if none is found
                    clean_url removes www. and sets the scheme to http://
                '''
                if raw_links:
                    links = [utils.clean_url(utils.set_domain(u, domain)) for u in raw_links]

                    if restrict:
                        links = filter(lambda x: utils.validate_domain(x, domain), links)

                    uncrawled_links.update(filter(lambda x: x not in crawled_links, links))

                crawled_links.add(url)
                print('Crawled {} (#{}).'.format(url, len(crawled_links)))
    except KeyboardInterrupt:
        pass

    # Optional filter keywords passed to --crawl option
    filter_words = args['crawl']
    if filter_words:
        return utils.filter_re(crawled_links, filter_words)

    return list(crawled_links)


def write_pages(args, links, file_name):
    if args['pdf']: 
        file_name = file_name + '.pdf'
        utils.clear_file(file_name)

        print('Attempting to write {} page(s) to {}.'.format(len(links), file_name))
        
        ''' Set pdfkit options
            Only ignore errors if there is more than one link
            This is to prevent an empty pdf being written
            But if links > 1 we don't want one failure to prevent writing others
        '''
        options = {}
        
        if len(links) > 1:
            options['ignore-load-errors'] = None

        if not args['verbose']:
            options['quiet'] = None

        try:
            pk.from_url(links, file_name, options=options)
        except Exception as e:
            sys.stderr.write('Could not convert to PDF.\n')
            sys.stderr.write(str(e) + '\n')
    else:
        file_name = file_name + '.txt'
        utils.clear_file(file_name)

        print('Attempting to write {} page(s) to {}.'.format(len(links), file_name))

        for link in links:
            html = utils.get_html(link)
            if len(html) > 0:
                text = utils.get_text(html, args['filter'])
                if text:
                    utils.write_file(text, file_name)
            else:
                sys.stderr.write('Failed to parse {}.\n'.format(link))


def scrape(args):
    for u in args['urls']:
        url = utils.resolve_url(u)

        domain = '{url.netloc}'.format(url=urlparse(url))
        args['domain'] = domain

        ''' Construct the output file name
            The proper extension will be added in write_pages
        '''
        base_url = domain.split('.')[-2]
        tail_url = url.strip('/').split('/')[-1]

        if base_url in tail_url:
            out_file = base_url
        else:
            out_file = base_url + '-' + tail_url

        if args['crawl'] or args['crawl_all']:
            links = crawl(args, url)
        else:
            links = [url]
        write_pages(args, links, out_file)


def command_line_runner():
    parser = get_parser()
    args = vars(parser.parse_args()) 

    if args['version']:
        print(__version__)
        return

    if not args['urls']:
        parser.print_help()
    else:
        scrape(args)



if __name__ == '__main__':
    command_line_runner()
