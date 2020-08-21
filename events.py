import re
import os
import requests as r
import config as cf
import tkinter as tk
import URLHIERARCHY as ur
from bs4 import BeautifulSoup as bs

def search(keyword):
    for i in range(len(ur.urls)):
        search_domain = ur.url_search_list[ur.urls[cf.url_index]]
        url = search_domain + keyword
        raw = r.get(url)

        html = bs(raw.content, 'html.parser')
        raw_results = html.find(id='ares')

        try:
            result_list = raw_results.findAll('table')
            for table in result_list:
                title_class = table.find(class_='d57')
                thumbnail_class = table.find(class_='d56 dlz')
                chapters_class = table.find(class_='d58')
                type_class = table.find(class_='d59')
                genre_class = table.find(class_='d60')

                manga_name = title_class.text
                domain_path = title_class.a['href']
                thumbnail = thumbnail_class['data-src']
                type = type_class.text
                chapters = chapters_class.text
                genre = genre_class.text

                print(manga_name)
                print(title_class)
                table = table.next_sibling

        except AttributeError:
            cf.url_index += 1
            print('I failed father')

        else:
            break

def temp():
    manga_domain = ur.url_domains["mangareader"]
    manga_domain = ur.url_domains[ur.urls[cf.url_index]] + domain_path
    raw_manga = r.get(manga_domain)
    html_manga = bs(raw_manga.content, 'html.parser')
    print(html_manga)
