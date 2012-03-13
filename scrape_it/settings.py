# Scrapy settings for scrape_it project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'scrape_it'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['scrape_it.spiders']
NEWSPIDER_MODULE = 'scrape_it.spiders'
DEFAULT_ITEM_CLASS = 'scrape_it.items.ScrapeItItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

