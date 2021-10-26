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

def cb_open_folder():
    global root
    rep = filedialog.askdirectory(
        parent=root,
        initialdir=os.getcwd())
    print(rep)

def cb_open_file():
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

def vw_button(x, y, text, callback ):
    b = ttk.Button(root, text=text,command=callback)
    b.place(x=x,y=y)
    return b

init()

vw_button(200, 100, "Open Folders", cb_open_folder)
vw_button(200, 150, "Open Files", cb_open_file)

start()
