import re
import os
import requests as r
import config as cf
import tkinter as tk
from bs4 import BeautifulSoup as bs

# command for <Return> key on search bar and search button
def search(keyword):
    # reseting the results
    for i in range(len(cf.button)):
        cf.button[i].pack_forget()

    # initializes/resets value
    cf.domain_path = []
    cf.chapters = []
    thumbnail = []
    type = []
    manga_name = []
    genre = []

    # runs for each site in the cf.urls list
    for i in range(len(cf.urls)):
        # gets the html content of the site
        url = cf.url_search_list[cf.urls[cf.url_index]] + keyword
        html = bs(r.get(url).content, 'html.parser')

        try:
            i = 0
            # gets the information on the results of the manga
            for table in html.find(id='ares').findAll('table'):

                manga_name.append(table.find(class_='d57').text)
                cf.domain_path.append(table.find(class_='d57').a['href'])
                thumbnail.append(table.find(class_='d56 dlz')['data-src'])
                type.append(table.find(class_='d59').text)
                cf.chapters.append(table.find(class_='d58').text)
                genre.append(table.find(class_='d60').text)

                cf.button[i].config(
                    text=manga_name[i] + '/n' + genre[i],
                    command=lambda choice=manga_name[i]: on_click(manga_name, choice)
                )

                cf.button[i].pack(side='top', anchor='nw')
                table = table.next_sibling
                i+=1
        # resets loop with a different url on next run
        except AttributeError as error:
            cf.url_index += 1
            print('I failed father', error)

        # ends loop on successful run
        else:
            break

# command for the chosen manga
def on_click(manga_title, choice):
    # gets the index of the chosen manga in the list of results
    index = manga_title.index(choice)
    # gets the latest chapter of the manga
    chapters = cf.chapters[index]
    # gets the manga domain
    cf.manga_domain = cf.url_domains[cf.urls[cf.url_index]] + cf.domain_path[index]
    html_manga = bs(r.get(cf.manga_domain).content, 'html.parser')

    # places the value in the placeholder
    for chapter in chapters:
        cf.c_buttons[chapter].config(
        text=chapter,
        command=lambda chapter_choice=chapter: manga_click(chapter_choice)
        )

# command for chosen chapter
def manga_click(chapter_choice):
    cf.manga_domain += '/' + str(chapter_choice)
    html_chapter = bs(r.get(cf.manga_domain))
    print(html_chapter.prettify())
