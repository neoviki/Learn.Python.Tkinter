try:
    import os
    import tkinter as tk
    import tkinter.ttk as ttk
    from tkinter import filedialog
except ImportError:
    import Tkinter as tk
    import ttk
    import tkFileDialog as filedialog

TITLE="demo"
WINDOW_BG='#555'
LABEL_BG="yellow"
FILE_TYPES=[('PDF files', '.pdf'),
            ('JPG files', '.jpg'),
            ('PNG files', '.png'),
            ('Py files', '*.py'),
            ('all files', '.*')]

root = None
style = None

def init():
    global root, style
    root = tk.Tk()
    root.configure(bg=WINDOW_BG)
    root.resizable(False, False)
    root.winfo_toplevel().title(TITLE)
    root.geometry('500x300')
    width = root.winfo_reqwidth()
    height = root.winfo_reqheight()

    px=int(root.winfo_screenwidth()/3 - width/2)
    py=int(root.winfo_screenheight()/3 - height/2)
    root.geometry('+{}+{}'.format(px, py))

    style = ttk.Style()
    style.theme_use("clam")

def start():
    global root
    root.mainloop()

def vw_input(x, y, font_size, input_width):
    global root
    entry = ttk.Entry(root)
    entry.config(width=input_width)
    entry.config(font=("Courier", font_size))
    entry.pack()
    entry.place(x=x,y=y)

init()
vw_input(100, 100, 15, 20)
start()

