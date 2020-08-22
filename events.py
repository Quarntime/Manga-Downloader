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
            i = 0
            for table in result_list:
                cf.title_class.append(table.find(class_='d57'))
                cf.thumbnail_class.append(table.find(class_='d56 dlz'))
                cf.chapters_class.append(table.find(class_='d58'))
                cf.type_class.append(table.find(class_='d59'))
                cf.genre_class.append(table.find(class_='d60'))

                manga_raw = cf.title_class[i]
                href_raw = cf.title_class[i]
                thumbnail_raw = cf.thumbnail_class[i]
                type_raw = cf.type_class[i]
                chapters_raw = cf.chapters_class[i]
                genre_raw = cf.genre_class[i]
                print(manga_raw, i)

                cf.manga_name.append(manga_raw.text)
                cf.domain_path.append(href_raw.a['href'])
                cf.thumbnail.append(thumbnail_raw['data-src'])
                cf.type.append(type_raw.text)
                cf.chapters.append(chapters_raw.text)
                cf.genre.append(genre_raw.text)

                table = table.next_sibling
                i+=1

        except AttributeError:
            cf.url_index += 1
            print('I failed father')

        else:
            break

def temp():
    manga_domain = ur.url_domains["mangareader"]
    manga_domain = ur.url_domains[ur.urls[cf.url_index]] + domain_path[cf.choice]
    raw_manga = r.get(manga_domain)
    html_manga = bs(raw_manga.content, 'html.parser')
    print(html_manga)
