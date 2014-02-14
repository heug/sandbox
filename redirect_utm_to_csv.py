#import modules
from urlparse import urlparse
import urllib2
import csv

#define the csv writer
file_name = open("redirects.csv", "wb")
c = csv.DictWriter(file_name, fieldnames=fieldnames, delimiter=',')
#define field names
fieldnames = ["link", "domain", "utm_source", "utm_medium", "utm_campaign"]
c.writerow(dict((fn, fn) for fn in fieldnames))

#pull dest url from origin url
def get_redirect(url):
	opener = urllib2.build_opener(urllib2.HTTPRedirectHandler)
	request = opener.open(url)
	return request.url

#loop!
for i in range(1, 1001):
	#empty the dictionary
	d = {}
	dest_url = get_redirect(link)

	#define origin url structure and set counter
	link = "http://www.website123.com/c/" + str(i)

	#parse dest url
	raw_parse = urlparse(dest_url, scheme='http')
	dom = raw_parse.netloc
	query = raw_parse.query

	#load info into dictionary
	d['link'] = link
	d['domain'] = dom
	d.update(item.split("=") for item in query.split("&"))
	
	#write to csv
	c.writerow(d)