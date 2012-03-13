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
	domains = [ #TODO add url/domain]
	urls = [
		 #TODO add url
	]

#second funtion..change any.html to required html file
	def parse(self, response):
		return [FormRequest.from_response(response,

						  data={"request": "RECHR"},
						  callback=self.parseList)]
	
	def parseList(self, response):
		self.log("Results after submitting form, ", level=log.INFO)
		with open("ANY.html, "w") as f:
			f.write(response.body)
		import os
		os.system("open ANY.html")
