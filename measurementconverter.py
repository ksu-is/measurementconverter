# Importing the modules
import tkinter as tk
from tkinter.constants import UNITS
import tkinter.font as font
from functools import partial
from tkinter import StringVar, messagebox
from tkinter import ttk

# Creating the window
window  =tk.Tk()
window.geometry('500x600')
window.title('Measurement Converter')
window.configure(bg = 'peach puff2')


# Creating the fonts
font1 = font.Font(family = 'helvetica',size = '30')
font2 = font.Font(family = 'helvetica',size = '10')
font3 = font.Font(family = 'helvetica',size = '20')

# creating unit converter label
main = tk.Label(window,text = 'Measurement Converter',bg = 'peach puff2')
main['font'] = font1
main.place(relx = '0.48',rely ='0.1', anchor = 'center')

#creating the mainloop
window.mainloop()

