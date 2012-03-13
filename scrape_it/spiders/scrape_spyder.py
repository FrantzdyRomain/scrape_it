#frantzdy romain
#frantzdy@kartvu.com
#scrape_spyder.py
#!/usr/bin/env/python
# encoding= utf-8

#import modules needed
from scrapy.spider import BaseSpider
from scrapy.http import Request
from scrapy.http import FormRequest
from scrapy.selector import HtmlXPathSelector

from scrapy import log
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

#create our class and inherit from BaseSpider
class ScrapeSpider(BaseSpider):
	name = "Scrape_It"
	domains = ["www.mtq.gouv.qc.ca"] #TODO
	urls = [
		 "http://www.mtq.gouv.qc.ca/pls/apex/f?p=102:56:::NO:RP::"
	]

	def parse(self, response):
		pass
