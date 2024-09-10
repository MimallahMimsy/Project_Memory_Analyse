from MemoryAnalyse import MemoryAnalyse
from tkinter import *


def search():
    big_size = ent1.get()
    dir = ent2.get()
    Find1 = MemoryAnalyse(big_size, dir)
    found_files = Find1.finder()
    n = len(found_files.keys())
    l3['text'] = f'Found {n} files'


root = Tk()
root.title("Memory Analyser")
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w // 2
h = h // 2
w = w + 50
h = h - 400
root.geometry(f'850x150+{w}+{h}')

f_top = Frame(root)
f_bot = Frame(root)

ent1 = Entry(f_top, width=20)
ent2 = Entry(f_bot, width=20)
but = Button(root, text='Search', command=search)
l1 = Label(f_top, width=50, text='Enter a value for a BIG file:')
l2 = Label(f_bot, width=80,
           text='Enter the path to the directory being examined; if the window is empty, the startup directory is examined:')
l3 = Label(root, width=20)
f_top.pack(pady=10)
f_bot.pack()

l1.pack(side=LEFT)
ent1.pack(side=LEFT)
l2.pack(side=LEFT)
ent2.pack(side=LEFT)
but.pack()
l3.pack()
root.mainloop()
