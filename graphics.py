# this is a branch

import events
import tkinter as tk
import config as cf
import ctypes

# Improves GUI graphics
if 'win' in tk.sys.platform:
    ctypes.windll.shcore.SetProcessDpiAwareness(True)

# Basic attributes of GUI
root = tk.Tk()
root.title('Manga Downloader')
root.minsize(cf.FWIDTH, cf.FHEIGHT)
root.geometry()

# Creates component of GUI and initializes
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

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side='right', fill='y')

# Creates placeholder for results
for _ in range(10):
    cf.thumbnail.append(tk.PhotoImage('Riniel.jpg', master=frame))
    cf.button.append(tk.Button(frame))

# Creates placeholder for mangas
for _ in range(100):
    cf.c_buttons.append(tk.Button(frame))

# Runs the tkinter program
root.mainloop()
