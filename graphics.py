# this is a branch

import events
import tkinter as tk
import config as cf
import ctypes

if 'win' in tk.sys.platform:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)

root = tk.Tk()

canvas = tk.Canvas(root, height=cf.FHEIGHT, width=cf.FWIDTH)
canvas.pack()

frame = tk.Frame(root, bg=cf.BGCOLOR)
frame.place(relwidth=1,relheight=.8,rely=.25)

label = tk.Label(root, text='Manga Downloader')
label.place(relheight=.1, relx=.01)

searchbar = tk.Entry(root)
searchbar.place(relx=.01, rely=.1, relwidth=.5)
searchbar.bind('<Return>', lambda event: events.search(keyword=searchbar.get()))

search = tk.Button(root, text='Search')
search.place(rely=.1 ,relx=.53, height=20)
search.config(command=lambda: events.search(keyword=searchbar.get()))

for title in cf.manga_name:



root.mainloop()
