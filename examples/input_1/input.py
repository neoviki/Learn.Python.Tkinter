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
main=None
root=None
# System Variables End

class MAIN:
    def __init__(self):
        global main
        self._TITLE='demo'
        self._BG_COLOR='#555'
        self._WIDTH=200
        self._HEIGHT=200
        self._DIMENSION='' + str(self._WIDTH) + 'x' + str(self._HEIGHT) + ''
        main = tk.Tk()
        self.bg(self._BG_COLOR)
        self.title(self._TITLE)
        self.dimension(self._WIDTH, self._HEIGHT)
        self.disable_resize()

    def dimension(self, w, h):
        global main
        self._WIDTH = str(w)
        self._HEIGHT = str(h)
        self._DIMENSION = '' + str(self._WIDTH) + 'x' + str(self._HEIGHT) + ''
        main.geometry(self._DIMENSION)
        w = main.winfo_reqwidth()
        h = main.winfo_reqheight()
        px=int(main.winfo_screenwidth()/3 - w/2)
        py=int(main.winfo_screenheight()/3 - h/2)
        main.geometry('+{}+{}'.format(px, py))

    def disable_resize(self):
        global main
        main.resizable(False, False)

    def enable_resize(self):
        global main
        main.resizable(True, True)

    def bg(self, bg_color):
        global main
        _BG_COLOR = bg_color
        main.configure(bg=_BG_COLOR)

    def title(self, title_string):
        global main, _TITLE
        _TITLE = title_string;
        main.winfo_toplevel().title(_TITLE)

    def gotoxy(self, x, y):
        global main
        main.geometry('+{}+{}'.format(x, y))

def BEGIN():
    global root, main
    root = MAIN()

def END():
    global main
    main.mainloop()


class input_box:
    def __init__(self):
        global main
        self.font_type = 'consolas'
        self.fsize = '12'
        self.width = 10
        self.height = 1
        self.bg_color = "white"
        self.fg_color = "black"
        self.border_color="black"
        self.object = tk.Entry(main)
        self.font(self.font_type)
        self.font_size(self.fsize)
        self.dimension(self.width, self.height)
        self.object.pack()

    def font(self, font_type):
        self.font_type = font_type
        self.object.config(font=(self.font_type, self.fsize))

    def font_size(self, fsize):
        self.fsize = str(fsize)
        self.object.config(font=(self.font_type, self.fsize))

    def bg(self, bg_color):
        self.bg_color = bg_color
        self.object.configure(bg=self.bg_color)

    def fg(self, fg_color):
        self.fg_color = fg_color
        self.object.configure(fg=self.fg_color)

    def gotoxy(self, x, y):
        self.object.place(x=x,y=y)

    def write(self, string):
        nstring=string
        self.object.insert(tk.END, nstring)

    def read(self):
        return self.object.get()

    def disable(self):
        self.object.configure(state='disabled')

    def enable(self):
        self.object.configure(state='normal')

    def dimension(self, w, h):
        self.width = w
        self.object.config(width=self.width)


BEGIN()

root.title("demo")
root.dimension(500,500)
root.bg('#555')
root.gotoxy(200,100)

obj = input_box()
obj.dimension(52, 1)
obj.gotoxy(30, 100)
obj.font_size(12)
obj.write("test")
obj.bg("red")
obj.fg("green")
print obj.read()
#obj.disable()
#obj.enable()

END()

