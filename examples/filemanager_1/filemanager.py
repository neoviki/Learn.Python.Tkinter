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

FILE_TYPES=[('PDF files', '.pdf'),
            ('JPG files', '.jpg'),
            ('PNG files', '.png'),
            ('Py files', '*.py'),
            ('all files', '.*')]

root = None

def init():
    global root
    root = tk.Tk()
    root.resizable(False, False)
    root.winfo_toplevel().title(TITLE)
    root.geometry('500x300')
    width = root.winfo_reqwidth()
    height = root.winfo_reqheight()

    px=int(root.winfo_screenwidth()/3 - width/2)
    py=int(root.winfo_screenheight()/3 - height/2)
    root.geometry('+{}+{}'.format(px, py))
    style = ttk.Style(root)
    style.theme_use("clam")

def open_folder():
    global root
    rep = filedialog.askdirectory(
        parent=root,
        initialdir=os.getcwd())
    print(rep)

def open_file():
    global root
    rep = filedialog.askopenfilenames(parent=root, initialdir=os.getcwd(), filetypes=FILE_TYPES)
    print(rep[0])
    #try:
    #    os.startfile(rep[0])
    #except IndexError:
    #    print("No file selected")

def start():
    global root
    root.mainloop()

init()

b1 = ttk.Button(root, text="Open Folders", command=open_folder)
b1.place(x=200,y=100)

b2 = ttk.Button(root, text="Open Files", command=open_file)
b2.place(x=200,y=150)

start()
