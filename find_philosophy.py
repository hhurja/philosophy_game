import urllib2
import cookielib
import re
from pprint import pprint
from pymongo import MongoClient


def scrape_site(url_input):
	link = url_input
	hdr = {'User-Agent' : 'Mozilla/5.0', 'Accept': 'text/html,applicatin/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
	req = urllib2.Request(link, headers=hdr)
	url = urllib2.urlopen(req)
	html = url.read()

	outFile = open('html.out', 'w')
	print >> outFile, html
	outFile.close()

	return html

def get_links(html):
	links = re.findall('(?<=<a href=")/wiki/.*?(?=\")', html)
	for link in links:
		print link


if __name__ == '__main__':
	title = 'not_philosophy'
	counter = 0
	titles = []
	link_beginning = 'https://en.wikipedia.org/wiki/'
	link_end = 'Special:Random'
	while title != 'Philosophy' and counter < 1:
		html_raw = scrape_site(link_beginning+link_end)
		title = re.findall('(?<=<title>).*\W-', html_raw)[0].rstrip(' -')
		# first_link = re.findall('<b>'+title[0]+'(.*?)href="/wiki/(.*?)"', html_raw)
		# print first_link[0]
		# link = 
		links = get_links(html_raw)
		counter += 1
		titles.append(title)
	print 'Found it after '+str(counter)+' attempt(s).'

	for t in titles:
		if t != 'Philosophy':
			print t+' --> '
		else:
			print t