import requests as r
import tkinter as tk
import config as cf
from bs4 import BeautifulSoup as bs

class Methods:
    def __init__(self,keyword, domain_path, chapters, thumbnail, type, manga_name, genre):
        self.keyword = keyword
        self.domain_path = domain_path
        self.chapters = chapters
        self.thumbnail = thumbnail
        self.type = type
        self.manga_name = manga_name
        self.genre = genre
        self.manga_domain = ''

        self.url_domains = {'mangareader': 'https://www.mangareader.net'}
        self.url_search_list = {
        'mangareader': 'https://www.mangareader.net/search/?nsearch=&msearch='
        }
        self.i = 0
        self.url = ''
        self.choice = ''
        self.html = bs()

    def initialize(self):
        url = self.url_search_list[cf.urls[cf.url_index]] + self.keyword
        self.html = bs(r.get(url).content, 'html.parser')


    def mangareader(self):
        for table in self.html.find(id='ares').findAll('table'):
            self.manga_name.append(table.find(class_='d57').text)
            self.domain_path.append(table.find(class_='d57').a['href'])
            self.thumbnail.append(table.find(class_='d56 dlz')['data-src'])
            self.type.append(table.find(class_='d59').text)
            self.chapters.append(table.find(class_='d58').text)
            self.genre.append(table.find(class_='d60').text)

            cf.button[self.i].config(
                text=self.manga_name[self.i] + '\n' + self.genre[self.i],
                command=lambda choice=self.manga_name[self.i]: self.mangareader_click(choice)
                )
            print(self.manga_name[self.i])

            cf.button[self.i].pack(side='top', anchor='nw')
            table = table.next_sibling
            self.i+=1


    def mangareader_click(self, userchoice):
        index = self.manga_name.index(self.choice)
        chapters = self.chapters[index]
        self.manga_domain = self.url_domains[cf.urls[cf.url_index]] + self.domain_path[index]
        html_manga = bs(r.get(self.manga_domain).content, 'html.parser')

        for chapter in chapters:
            cf.c_buttons[chapter].config(
            text=chapter,
            command=lambda chapter_choice=chapter: self.manga_click(chapter_choice)
            )

    def manga_click(self):
        self.manga_domain += '/' + str(chapter_choice)
        html_chapter = bs(r.get(self.mangadomain).content)
        print(html_chapter.prettify())
