import re
import os
import requests as r
import config as cf
import tkinter as tk
import URLHIERARCHY as ur
from bs4 import BeautifulSoup as bs

def search(keyword):
    Runtime = False
    title_class = []
    thumbnail_class = []
    chapters_class = []
    type_class = []
    genre_class = []

    manga_name = []
    domain_path = []
    thumbnail = []
    type = []
    chapters = []
    genre = []
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
                title_class.append(table.find(class_='d57'))
                thumbnail_class.append(table.find(class_='d56 dlz'))
                chapters_class.append(table.find(class_='d58'))
                type_class.append(table.find(class_='d59'))
                genre_class.append(table.find(class_='d60'))

                manga_raw = title_class[i]
                href_raw = title_class[i]
                thumbnail_raw = thumbnail_class[i]
                type_raw = type_class[i]
                chapters_raw = chapters_class[i]
                genre_raw = genre_class[i]

                manga_name.append(manga_raw.text)
                domain_path.append(href_raw.a['href'])
                thumbnail.append(thumbnail_raw['data-src'])
                type.append(type_raw.text)
                chapters.append(chapters_raw.text)
                genre.append(genre_raw.text)

                cf.button[i].config(text=manga_name[i])
                cf.button[i].pack(side='top')
                table = table.next_sibling
                i+=1

                print(manga_name)

        except AttributeError as error:
            cf.url_index += 1
            print('I failed father', error)

        else:
            break

def on_click(choice):

    manga_domain = ur.url_domains["mangareader"]
    manga_domain = ur.url_domains[ur.urls[url_index]] + domain_path[choice]
    raw_manga = r.get(manga_domain)
    html_manga = bs(raw_manga.content, 'html.parser')
    print(html_manga)
