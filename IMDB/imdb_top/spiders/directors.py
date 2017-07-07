# -*- coding: utf-8 -*-
import scrapy
import json


class DirectorsSpider(scrapy.Spider):
    name = 'directors'
    allowed_domains = ['imdb.com']
    start_urls = []


    with open('imdb_top_movies.json') as f:
    	r=f.read()
    	d=json.loads(r)
    	for i in range(10):
    		start_urls.append(d[i]['link'])

    def parse(self, response):
        yield{
        "movie": response.css('div.title_wrapper h1::text').extract_first(),
        "director": response.css('div.credit_summary_item span.itemprop::text').extract_first()
        }
