# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 10:18:27 2022

@author: TalipovaOV
"""
from urllib import response
import scrapy
import time

class ObrazSpider(scrapy.Spider):
    name = "ObrazSpider"
    start_urls = ["https://obrazoval.ru/f/programmirovanie"]
    
    
    def parse(self, response):
        links = response.css('a.b-title__course.l-course__title.block::attr(href)').getall()
        for link in links:
            time.sleep(5)
            yield response.follow(link, self.parse_curs)

        linkAdd = response.css("a.b-btn.b-btn--secondary.full-width::attr(href)").get()
        yield response.follow(linkAdd, self.parse)

    

    def parse_curs(self, response):
        yield {
            "name": response.css("div.text-h2-bold.q-mb-xs.lt-md::text").get(),
            "price": response.css("div.text-h0-bold span::text").get().split("₽")[0].strip().replace("\xa0",""),
            "duration": response.css("div.flex.items-center::text").get().split()[0],
            "rating": response.css("div.text-h4.l-course__position::text").get(),
            "level": response.css("div.l-features__value::text")[0].get(),
            "employment" : response.css("div.l-features__value::text")[3].get(),
            "certificate": response.css("div.l-features__value::text")[4].get(),
            "skills" : response.css("div.l-skills__item-name::text").getall(),
            "skillsA": response.css("a.l-skills__item-name::text").getall(),
            "owners": response.css("div.owners-list__item-header a::text").get()
            }