import re
import os
import requests as r
import config as cf
import tkinter as tk
from bs4 import BeautifulSoup as bs

def search(keyword):
    for i in range(len(cf.button)):
        cf.button[i].pack_forget()

    Runtime = False
    title_class = []
    thumbnail_class = []
    chapters_class = []
    type_class = []
    genre_class = []

    manga_name = []
    cf.domain_path = []
    thumbnail = []
    type = []
    chapters = []
    genre = []
    for i in range(len(cf.urls)):
        search_domain = cf.url_search_list[cf.urls[cf.url_index]]
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

                manga_name.append(title_class[i].text)
                cf.domain_path.append(title_class[i].a['href'])
                thumbnail.append(thumbnail_class[i]['data-src'])
                type.append(type_class[i].text)
                chapters.append(chapters_class[i].text)
                genre.append(genre_class[i].text)

                print(thumbnail_class)

                cf.button[i].config(
                    text=manga_name[i],
                    command=lambda choice=manga_name[i]: on_click(manga_name, choice)
                )

                cf.button[i].pack(side='top', anchor='nw')
                table = table.next_sibling
                i+=1

                print(manga_name)

        except AttributeError as error:
            cf.url_index += 1
            print('I failed father', error)

        else:
            break

def on_click(manga_title, choice):
    index = manga_title.index(choice)
    manga_domain = cf.url_domains[cf.urls[cf.url_index]] + cf.domain_path[index]
    raw_manga = r.get(manga_domain)
    html_manga = bs(raw_manga.content, 'html.parser')
    print(html_manga.prettify())
