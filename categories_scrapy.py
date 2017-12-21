#! /usr/bin/env python3
# coding: utf-8

"""
File to save categeries from OpenFoodFacts
"""

import scrapy

class CategoriesSpider(scrapy.Spider):
    name = 'categories'
    start_urls = ['https://fr.openfoodfacts.org/categories/']

    def parse(self, response):
        for link in response.css('tbody tr'):
            if link.css('a.tag.well_known::text').extract_first() != None:
                yield {'category': link.css('a.tag.well_known::text').extract_first()}
