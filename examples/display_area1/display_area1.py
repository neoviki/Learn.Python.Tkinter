try:
    import os
    import tkinter as tk
    import tkinter.ttk as ttk
    from tkinter import filedialog
    import tkinter.scrolledtext as scrolledtext
    import tkFont
except ImportError:
    import Tkinter as tk
    import ttk
    import tkFileDialog as filedialogs
    import Tkinter.scrolledtext as scrolledtext
    import tkFont


# System Variables Start

TITLE="demo"
root=None
_TITLE='demo'
_BG_COLOR='#555'
_WIDTH=10
_HEIGHT=10
_DIMENSION='' + str(_WIDTH) + 'x' + str(_HEIGHT) + ''

# System Variables End

def dimension(w, h):
    global root, _WIDTH, _HEIGHT, _DIMENSION
    _WIDTH = str(w)
    _HEIGHT = str(h)
    _DIMENSION = '' + str(_WIDTH) + 'x' + str(_HEIGHT) + ''
    root.geometry(_DIMENSION)
    w = root.winfo_reqwidth()
    h = root.winfo_reqheight()
    px=int(root.winfo_screenwidth()/3 - w/2)
    py=int(root.winfo_screenheight()/3 - h/2)
    root.geometry('+{}+{}'.format(px, py))

def resizable(flag):
    global root
    root.resizable(flag, flag)

def bg(bg_color):
    global root, _BG_COLOR
    _BG_COLOR = bg_color
    root.configure(bg=_BG_COLOR)

def title(title_string):
    global root, _TITLE
    _TITLE = title_string;
    root.winfo_toplevel().title(_TITLE)

def loop():
    global root
    root.mainloop()

def gotoxy(x, y):
    global root
    root.geometry('+{}+{}'.format(x, y))

def init(w, h):
    global root, _BG_COLOR, _TITLE, _WIDTH, _HEIGHT, _DIMENSION
    root = tk.Tk()
    bg(_BG_COLOR)
    title(_TITLE)
    dimension(w, h)
    resizable(False)

class display_area:
    def __init__(self,win):
        self.font_type = 'consolas'
        self.fsize = '12'
        self.width = 10
        self.height = 10
        self.bg_color = "white"
        self.fg_color = "black"
        self.border_color="black"

        self.display = scrolledtext.ScrolledText(master=win,
                                                 cursor="arrow",
                                                 bg=self.bg_color,
                                                 undo=True,
                                                 wrap=tk.WORD)

        self.display.configure(width=self.width, height=self.height)

        self.display['font'] = (self.font_type, self.fsize)
        self.display.configure(highlightbackground=self.border_color)
        self.display.configure(state='disabled')
        self.display.pack()

    def font(self, font_type):
        self.font_type = font_type
        self.display['font'] = (self.font_type, self.font_size)

    def font_size(self, fsize):
        self.fsize = str(fsize)
        self.display['font'] = (self.font_type, self.fsize)

    def bg(self, bg_color):
        self.bg_color = bg_color
        self.display.configure(bg=self.bg_color)
        return

    def gotoxy(self, x, y):
        self.display.place(x=x,y=y)

    def println(self, string):
        self.display.configure(state='normal')
        nstring=" " + string + '\n'
        self.display.insert(tk.END, nstring)
        self.display.configure(state='disabled')

    def dimension(self, w, h):
        self.width = w
        self.height = h
        self.display.configure(width=self.width, height=self.height)




init(500, 500)

title("demo")
bg('#555')
gotoxy(600,100)
d = display_area(root)
d.dimension(52, 10)
d.gotoxy(30, 100)
d.font_size(13)
d.println("test")
d.bg("red")

loop()

