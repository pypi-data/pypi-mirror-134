import tkinter as tk
# from tkinter import *
from tkinter import ttk


class MainWindow:
    def __init__(self):
        window = tk.Tk()
        window.geometry("1024x550")
        window.title("PyRho - Control Earth Resistivity Meter")

        tabControl = ttk.Notebook(window)
        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab1,text='Tab 1')
        tabControl.add(tab2, text = 'Tab 2')
        tabControl.pack(expand=1, fill="both")

        window.mainloop()


if __name__ == '__main__':
    MainWindow()
