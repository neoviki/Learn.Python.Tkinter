try:
    import os
    import tkinter as tk
    import tkinter.ttk as ttk
    from tkinter import filedialog
    import tkinter.scrolledtext as scrolledtext
except ImportError:
    import Tkinter as tk
    import ttk
    import tkFileDialog as filedialogs
    import Tkinter.scrolledtext as scrolledtext

TITLE="demo"
WINDOW_BG='#555'
DISPLAY_AREA_BG="white"
DISPLAY_AREA_BORDER="black"
DISPLAY_AREA_FONT_SIZE='12'
DISPLAY_AREA_FONT='consolas'

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

def display_area(x, y, width, height):
    global root
    display = scrolledtext.ScrolledText(master=root, cursor="arrow", bg=DISPLAY_AREA_BG,
                                        undo=True, wrap=tk.WORD, width=width, height=height)
    display['font'] = (DISPLAY_AREA_FONT, DISPLAY_AREA_FONT_SIZE)
    display.configure(highlightbackground=DISPLAY_AREA_BORDER)
    display.configure(state='disabled')
    display.pack()
    display.place(x=x,y=y)
    return display

def display_areas_print(handle, string):
    handle.configure(state='normal')
    nstring=" " + string + '\n'
    handle.insert(tk.END, nstring)
    handle.configure(state='disabled')

d = display_area(30, 100, 52, 10)
for i in range(20):
    display_areas_print(d, "test")


start()
