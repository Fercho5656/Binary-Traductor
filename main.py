import traductor
from tkinter import *
import tkinter.font as tkFont


class MainGUI(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.parent = master
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        title_font = tkFont.Font(family='Arial Bold', size=25, weight='bold')
        default_font = tkFont.Font(family='Arial Bold', size=18, weight='bold')

        label_title = Label(
            self, text='Traductor Binario-Texto Texto-Binario', font=title_font)
        label_bin_to_text = Label(
            self, text='Binario a Texto', font=default_font)
        label_text_to_bin = Label(
            self, text='Texto a Binario', font=default_font)
        label_result = Label(self, text='Traducción', font=default_font)

        text_result = StringVar()

        entry_bin_to_text = Entry(self, width=50, font=default_font)
        entry_text_to_bin = Entry(self, width=50, font=default_font)
        entry_result = Entry(
            self, width=50, font=default_font, textvariable=text_result)
        entry_result.config(state=DISABLED)

        btn_bin_to_text = Button(
            self, text='Traducir', font=default_font, command=lambda: bin_to_text())
        btn_text_to_bin = Button(
            self, text='Traducir', font=default_font, command=lambda: text_to_bin())

        label_title.grid(column=0, row=0)

        label_bin_to_text.grid(column=0, row=1)
        entry_bin_to_text.grid(column=1, row=1)
        btn_bin_to_text.grid(column=2, row=1)

        label_text_to_bin.grid(column=0, row=2)
        entry_text_to_bin.grid(column=1, row=2)
        btn_text_to_bin.grid(column=2, row=2)

        label_result.grid(column=0, row=3)
        entry_result.grid(column=1, row=3)

        def bin_to_text():
            text_result.set(traductor.bin_to_text(entry_bin_to_text.get()))

        def text_to_bin():
            text_result.set(traductor.text_to_bin(entry_text_to_bin.get()))


Traductor = Tk()
Traductor.title('Practica Unidad 2')
Traductor.resizable(False, False)
root = MainGUI(Traductor).grid()
Traductor.mainloop()
