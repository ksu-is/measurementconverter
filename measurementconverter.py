# Importing the modules
from curses import COLOR_BLACK
import tkinter as tk
from tkinter.constants import UNITS
import tkinter.font as font
from functools import partial
from tkinter import Image, StringVar, messagebox
from tkinter import ttk

# Creating the window
window  =tk.Tk()
window.geometry('400x500')
window.title('Measurement Converter')
window.configure(bg = 'gray')

# Creating the fonts
font1 = font.Font(family = 'helvetica bold',size = '30')
font2 = font.Font(family = 'helvetica',size = '10')
font3 = font.Font(family = 'helvetica',size = '20')
font4 = font.Font(family = 'helvetica',size = '12')

# The textvariables
number_from = StringVar()

# All the functions
# Fromfunc function
def fromfunc(event):
    global result_from
    result_from = event.widget.get()

# Tofunc function
def tofunc(event):
    global result_to
    result_to = event.widget.get()


# The answer function
def answer(n1):
    num1 = n1.get()
    try:
        number1 = int(num1)
    except:
        messagebox.showerror('Error','Term not recognised')

    # Volume conversions
    if result_from == 'Cubic meters' and result_to == 'Cubic meters':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Cubic meters' and result_to == 'Cubic foot':
        calculate = number1*35.3147
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Cubic meters' and result_to == 'Liters':
        calculate = number1*1000
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Cubic meters' and result_to == 'U.S. Gallon':
        calculate = number1*264.172
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Cubic meters' and result_to == 'Cubic centimeters':
        calculate = number1*1000000
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Cubic foot' and result_to == 'Cubic meters':
        calculate = number1*0.02831
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Cubic foot' and result_to == 'Cubic foot':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Cubic foot' and result_to == 'Liters':
        calculate = number1*28.31679
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Cubic foot' and result_to == 'U.S. Gallon':
        calculate = number1*7.4805
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Cubic foot' and result_to == 'Cubic centimeters':
        calculate = number1*28316.8
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Liters' and result_to == 'Cubic meters':
        calculate = number1*0.000999
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Liters' and result_to == 'Cubic foot':
        calculate = number1*0.0353146
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Liters' and result_to == 'Liters':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Liters' and result_to == 'U.S. Gallon':
        calculate = number1*0.26417
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Liters' and result_to == 'Cubic centimeters':
        calculate = number1*1000
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'U.S. Gallon' and result_to == 'Cubic meters':
        calculate = number1*0.003785
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'U.S. Gallon' and result_to == 'Cubic foot':
        calculate = number1*0.13368
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'U.S. Gallon' and result_to == 'Liters':
        calculate = number1*3.7854
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'U.S. Gallon' and result_to == 'U.S. Gallon':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'U.S. Gallon' and result_to == 'Cubic centimeters':
        calculate = number1*3786.41
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Cubic centimeters' and result_to == 'Cubic meters':
        calculate = number1*9.99999
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Cubic centimeters' and result_to == 'Cubic foot':
        calculate = number1*3.53146
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Cubic centimeters' and result_to == 'Liters':
        calculate = number1*0.000999
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Cubic centimeters' and result_to == 'Cubic meters':
        calculate = number1*9.9999
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Cubic centimeters' and result_to == 'Liters':
        calculate = number1*0.00099999
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Cubic centimeters' and result_to == 'U.S. Gallon':
        calculate = number1*0.00026417
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Cubic centimeters' and result_to == 'Cubic centimeters':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'U.S. Cup' and result_to == 'U.S. Cup':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'U.S. Cup' and result_to == 'Cubic centimeters':
        calculate = number1*236.6
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'U.S. Cup' and result_to == 'Cubic meters':
        calculate = number1/4227
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'U.S. Cup' and result_to == 'Liters':
        calculate = number1/4.227
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'U.S. Cup' and result_to == 'U.S. Gallon':
        calculate = number1/16
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'U.S. Cup' and result_to == 'Imperial Cup':
        calculate = number1/1.201
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'U.S. Cup' and result_to == 'Imperial Gallon':
        calculate = number1/19.215
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'U.S. Cup' and result_to == 'Cubic foot':
        calculate = number1/119.7
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Cubic foot' and result_to == 'U.S. Cup':
        calculate = number1*119.7
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Imperial Cup' and result_to == 'U.S. Cup':
        calculate = number1*1.201
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Imperial Cup' and result_to == 'Cubic centimeters':
        calculate = number1*284.1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Imperial Cup' and result_to == 'Cubic meters':
        calculate = number1/3250
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Imperial Cup' and result_to == 'Liters':
        calculate = number1/3.52
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Imperial Cup' and result_to == 'U.S. Gallon':
        calculate = number1/13.323
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Imperial Cup' and result_to == 'Imperial Cup':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Imperial Cup' and result_to == 'Imperial Gallon':
        calculate = number1/16
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Imperial Cup' and result_to == 'Cubic foot':
        calculate = number1/99.661
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Cubic foot' and result_to == 'Imperial Cup':
        calculate = number1*99.661
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Imperial Gallon' and result_to == 'U.S. Cup':
        calculate = number1*18.942
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Imperial Gallon' and result_to == 'Cubic centimeters':
        calculate = number1*4546
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Imperial Gallon' and result_to == 'Cubic meters':
        calculate = number1/220
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Imperial Gallon' and result_to == 'Liters':
        calculate = number1*4.546
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Imperial Gallon' and result_to == 'U.S. Gallon':
        calculate = number1*1.201
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Imperial Gallon' and result_to == 'Imperial Cup':
        calculate = number1*16
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Imperial Gallon' and result_to == 'Imperial Gallon':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Cubic Centimeters' and result_to == 'U.S. Cup':
        calculate = number1/236.6
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Cubic meters' and result_to == 'U.S. Cup':
        calculate = number1*4227
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Liters' and result_to == 'U.S. Cup':
        calculate = number1*4.227
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'U.S. Gallon' and result_to == 'U.S. Cup':
        calculate = number1*16
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Imperial Cup' and result_to == 'U.S. Cup':
        calculate = number1*1.201
        result.cget('text')
        result.configure(text = (calculate,result_to))
 
    elif result_from == 'Imperial Gallon' and result_to == 'Cubic foot':
        calculate = number1/6.229
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Cubic foot' and result_to == 'Imperial Gallon':
        calculate = number1*6.229
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'U.S. Cup' and result_to == 'Imperial Gallon':
        calculate = number1/18.942
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Cubic centimeters' and result_to == 'Imperial Gallon':
        calculate = number1/4546
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Cubic meters' and result_to == 'Imperial Gallon':
        calculate = number1*220
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Liters' and result_to == 'Imperial Gallon':
        calculate = number1/4.546
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'U.S. Gallon' and result_to == 'Imperial Gallon':
        calculate = number1/1.201
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Imperial Gallon' and result_to == 'Imperial Cup':
        calculate = number1*16
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'U.S. Cup' and result_to == 'Imperial Cup':
        calculate = number1/1.201
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Cubic centimeters' and result_to == 'Imperial Cup':
        calculate = number1/284.1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Cubic meters' and result_to == 'Imperial Cup':
        calculate = number1*3250
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Liters' and result_to == 'Imperial Cup':
        calculate = number1*3.52
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'U.S. Gallon' and result_to == 'Imperial Cup':
        calculate = number1*13.323
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Imperial Gallon' and result_to == 'Imperial Cup':
        calculate = number1*16
        result.cget('text')
        result.configure(text = (calculate,result_to))

    #length conversions

    elif result_from == 'Millimeters' and result_to == 'Millimeters':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Millimeters' and result_to == 'Centimeters':
        calculate = number1/10
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Millimeters' and result_to == 'Decimeters':
        calculate = number1/100
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Millimeters' and result_to == 'Meters':
        calculate = number1/1000
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Millimeters' and result_to == 'Kilometers':
        calculate = number1/1e+6
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Millimeters' and result_to == 'Mile':
        calculate = number1/1.609e+6
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Millimeters' and result_to == 'Foot':
        calculate = number1/304.8
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Millimeters' and result_to == 'Yard':
        calculate = number1/914.4
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Millimeters' and result_to == 'Inch':
        calculate = number1/25.4
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Centimeters' and result_to == 'Centimeters':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Centimeters' and result_to == 'Millimeters':
        calculate = number1*10
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Centimeters' and result_to == 'Decimeters':
        calculate = number1/10
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Centimeters' and result_to == 'Meters':
        calculate = number1/100
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Centimeters' and result_to == 'Kilometers':
        calculate = number1/100000
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Centimeters' and result_to == 'Mile':
        calculate = number1/160900
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Centimeters' and result_to == 'Foot':
        calculate = number1/30.48
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Centimeters' and result_to == 'Yard':
        calculate = number1/91.44
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Centimeters' and result_to == 'Inch':
        calculate = number1/2.54
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Decimeters' and result_to == 'Decimeters':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Decimeters' and result_to == 'Millimeters':
        calculate = number1*100
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Decimeters' and result_to == 'Centimeters':
        calculate = number1*10
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Decimeters' and result_to == 'Meters':
        calculate = number1/10
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Decimeters' and result_to == 'Kilometers':
        calculate = number1/10000
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Decimeters' and result_to == 'Mile':
        calculate = number1/16090
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Decimeters' and result_to == 'Foot':
        calculate = number1/3.048
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Decimeters' and result_to == 'Yard':
        calculate = number1/9.144
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Decimeters' and result_to == 'Inch':
        calculate = number1*3.937
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Meters' and result_to == 'Meters':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Meters' and result_to == 'Decimeters':
        calculate = number1*10
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Meters' and result_to == 'Millimeters':
        calculate = number1*1000
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Meters' and result_to == 'Centimeters':
        calculate = number1*100
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Meters' and result_to == 'Kilometers':
        calculate = number1/1000
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Meters' and result_to == 'Mile':
        calculate = number1/1609
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Meters' and result_to == 'Foot':
        calculate = number1*3.281
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Meters' and result_to == 'Yard':
        calculate = number1*1.094
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Meters' and result_to == 'Inch':
        calculate = number1*39.37
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Kilometers' and result_to == 'Kilometers':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'Kilometers' and result_to == 'Meters':
        calculate = number1*1000
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Kilometers' and result_to == 'Decimeters':
        calculate = number1*10000
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Kilometers' and result_to == 'Millimeters':
        calculate = number1*1e+6
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Kilometers' and result_to == 'Centimeters':
        calculate = number1*100000
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Kilometers' and result_to == 'Mile':
        calculate = number1/1.609
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Kilometers' and result_to == 'Foot':
        calculate = number1*3281
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Kilometers' and result_to == 'Yard':
        calculate = number1*1094
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Kilometers' and result_to == 'Inch':
        calculate = number1*39370
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Mile' and result_to == 'Mile':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Mile' and result_to == 'Kilometers':
        calculate = number1*1.609
        result.cget('text')
        result.configure(text = (calculate,result_to))
    elif result_from == 'Mile' and result_to == 'Meters':
        calculate = number1*1609
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Mile' and result_to == 'Decimeters':
        calculate = number1*16090
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Mile' and result_to == 'Millimeters':
        calculate = number1*1.609e+6
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Mile' and result_to == 'Centimeters':
        calculate = number1*160900
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Mile' and result_to == 'Foot':
        calculate = number1*5280
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Mile' and result_to == 'Yard':
        calculate = number1*1760
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Mile' and result_to == 'Inch':
        calculate = number1*63360
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Yard' and result_to == 'Yard':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Yard' and result_to == 'Mile':
        calculate = number1/1760
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Yard' and result_to == 'Kilometers':
        calculate = number1/1094
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Yard' and result_to == 'Meters':
        calculate = number1/1.094
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Yard' and result_to == 'Decimeters':
        calculate = number1*9.144
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Yard' and result_to == 'Millimeters':
        calculate = number1*914.4
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Yard' and result_to == 'Centimeters':
        calculate = number1*91.44
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Yard' and result_to == 'Foot':
        calculate = number1*3
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Yard' and result_to == 'Inch':
        calculate = number1*36
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Foot' and result_to == 'Foot':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))    
    
    elif result_from == 'Foot' and result_to == 'Yard':
        calculate = number1/3
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Foot' and result_to == 'Mile':
        calculate = number1/5280
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Foot' and result_to == 'Kilometers':
        calculate = number1/3281
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Foot' and result_to == 'Meters':
        calculate = number1/3.281
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Foot' and result_to == 'Decimeters':
        calculate = number1*3.048
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Foot' and result_to == 'Millimeters':
        calculate = number1*304.8
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Foot' and result_to == 'Centimeters':
        calculate = number1*30.48
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Foot' and result_to == 'Inch':
        calculate = number1*12
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Inch' and result_to == 'Inch':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Inch' and result_to == 'Foot':
        calculate = number1/12
        result.cget('text')
        result.configure(text = (calculate,result_to))    
    
    elif result_from == 'Inch' and result_to == 'Yard':
        calculate = number1/36
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Inch' and result_to == 'Mile':
        calculate = number1/63360
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Inch' and result_to == 'Kilometers':
        calculate = number1/39370
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Inch' and result_to == 'Meters':
        calculate = number1/39.37
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Inch' and result_to == 'Decimeters':
        calculate = number1/3.937
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Inch' and result_to == 'Millimeters':
        calculate = number1*25.4
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Inch' and result_to == 'Centimeters':
        calculate = number1*2.54
        result.cget('text')
        result.configure(text = (calculate,result_to))

# mass conversions

    elif result_from == 'Milligrams' and result_to == 'Milligrams':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Milligrams' and result_to == 'Centigrams':
        calculate = number1/10
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Milligrams' and result_to == 'Grams':
        calculate = number1/1000
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Milligrams' and result_to == 'Decigrams':
        calculate = number1/100
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Milligrams' and result_to == 'Kilograms':
        calculate = number1/1e+6
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Milligrams' and result_to == 'Metric ton':
        calculate = number1/1e+9
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Milligrams' and result_to == 'U.S. ton':
        calculate = number1/9.072e+8
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Milligrams' and result_to == 'Imperial ton':
        calculate = number1/1.016e+9
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Milligrams' and result_to == 'Pound':
        calculate = number1/453600
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Milligrams' and result_to == 'Ounce':
        calculate = number1/28350
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Centigrams' and result_to == 'Milligrams':
        calculate = number1*10
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Centigrams' and result_to == 'Centigrams':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Centigrams' and result_to == 'Grams':
        calculate = number1/100
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Centigrams' and result_to == 'Decigrams':
        calculate = number1/10
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Centiigrams' and result_to == 'Kilograms':
        calculate = number1/100000
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Centigrams' and result_to == 'Metric ton':
        calculate = number1/1e+8
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Centigrams' and result_to == 'U.S. ton':
        calculate = number1/9.072e+7
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Centigrams' and result_to == 'Imperial ton':
        calculate = number1/1.016e+8
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Centigrams' and result_to == 'Pound':
        calculate = number1/45360
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Centigrams' and result_to == 'Ounce':
        calculate = number1/2835
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Grams' and result_to == 'Milligrams':
        calculate = number1*1000
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Grams' and result_to == 'Centigrams':
        calculate = number1*100
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Grams' and result_to == 'Grams':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Grams' and result_to == 'Decigrams':
        calculate = number1*10
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Grams' and result_to == 'Kilograms':
        calculate = number1/1000
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Grams' and result_to == 'Metric ton':
        calculate = number1/1e+6
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Grams' and result_to == 'U.S. ton':
        calculate = number1/907200
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Grams' and result_to == 'Imperial ton':
        calculate = number1/1.016e+6
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Grams' and result_to == 'Pound':
        calculate = number1/453.6
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Grams' and result_to == 'Ounce':
        calculate = number1/28.35
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Decigrams' and result_to == 'Milligrams':
        calculate = number1*100
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Deciigrams' and result_to == 'Centigrams':
        calculate = number1*10
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Decigrams' and result_to == 'Grams':
        calculate = number1/10
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Decigrams' and result_to == 'Decigrams':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Decigrams' and result_to == 'Kilograms':
        calculate = number1/10000
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Decigrams' and result_to == 'Metric ton':
        calculate = number1/1e+7
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Decigrams' and result_to == 'U.S. ton':
        calculate = number1/9.072e+6
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Decigrams' and result_to == 'Imperial ton':
        calculate = number1/1.016e+7
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Decigrams' and result_to == 'Pound':
        calculate = number1/4536
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Decigrams' and result_to == 'Ounce':
        calculate = number1/283.5
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Kilograms' and result_to == 'Milligrams':
        calculate = number1*1e+6
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Kilograms' and result_to == 'Centigrams':
        calculate = number1*100000
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Kilograms' and result_to == 'Grams':
        calculate = number1*1000
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Kilograms' and result_to == 'Decigrams':
        calculate = number1*10000
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Kilograms' and result_to == 'Kilograms':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Kilograms' and result_to == 'Metric ton':
        calculate = number1/1000
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Kilograms' and result_to == 'U.S. ton':
        calculate = number1/907.2
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Kilograms' and result_to == 'Imperial ton':
        calculate = number1/1016
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Kilograms' and result_to == 'Pound':
        calculate = number1*2.205
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Kilograms' and result_to == 'Ounce':
        calculate = number1*35.274
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Metric ton' and result_to == 'Milligrams':
        calculate = number1*1e+9
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Metric ton' and result_to == 'Centigrams':
        calculate = number1*1e+8
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Metric ton' and result_to == 'Grams':
        calculate = number1*1e+6
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Metric ton' and result_to == 'Decigrams':
        calculate = number1/1e+7
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Metric ton' and result_to == 'Kilograms':
        calculate = number1*1000
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Metric ton' and result_to == 'Metric ton':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Metric ton' and result_to == 'U.S. ton':
        calculate = number1*1.102
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Metric ton' and result_to == 'Imperial ton':
        calculate = number1/1.016
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Metric ton' and result_to == 'Pound':
        calculate = number1*2205
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Metric ton' and result_to == 'Ounce':
        calculate = number1*35270
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'U.S. ton' and result_to == 'Milligrams':
        calculate = number1*9.072e+8
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'U.S. ton' and result_to == 'Centigrams':
        calculate = number1*9.072e+7
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'U.S. ton' and result_to == 'Grams':
        calculate = number1*907200
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'U.S. ton' and result_to == 'Decigrams':
        calculate = number1*9.072e+6
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'U.S. ton' and result_to == 'Kilograms':
        calculate = number1*907.2
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'U.S. ton' and result_to == 'Metric ton':
        calculate = number1/1.102
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'U.S. ton' and result_to == 'U.S. ton':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'U.S. ton' and result_to == 'Imperial ton':
        calculate = number1/1.12
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'U.S. ton' and result_to == 'Pound':
        calculate = number1*2000
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'U.S. ton' and result_to == 'Ounce':
        calculate = number1*32000
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Imperial ton' and result_to == 'Milligrams':
        calculate = number1*1.016e+9
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Imperial ton' and result_to == 'Centigrams':
        calculate = number1*1.016e+8
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Imperial ton' and result_to == 'Grams':
        calculate = number1*1.016e+6
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Imperial ton' and result_to == 'Decigrams':
        calculate = number1*1.016e+7
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Imperial ton' and result_to == 'Kilograms':
        calculate = number1*1016
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Imperial ton' and result_to == 'Metric ton':
        calculate = number1*1.016
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Imperial ton' and result_to == 'U.S. ton':
        calculate = number1*1.12
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Imperial ton' and result_to == 'Imperial ton':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Imperial ton' and result_to == 'Pound':
        calculate = number1*2240
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Imperial ton' and result_to == 'Ounce':
        calculate = number1*35840
        result.cget('text')
        result.configure(text = (calculate,result_to))
        
    elif result_from == 'Pound' and result_to == 'Milligrams':
        calculate = number1*453592
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Pound' and result_to == 'Centigrams':
        calculate = number1*45360
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Pound' and result_to == 'Grams':
        calculate = number1*453.6
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Pound' and result_to == 'Decigrams':
        calculate = number1*4536
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Pound' and result_to == 'Kilograms':
        calculate = number1/2.205
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Pound' and result_to == 'Metric ton':
        calculate = number1/2205
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Pound' and result_to == 'U.S. ton':
        calculate = number1/2000
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Pound' and result_to == 'Imperial ton':
        calculate = number1/2240
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Pound' and result_to == 'Pound':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Pound' and result_to == 'Ounce':
        calculate = number1*16
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Ounce' and result_to == 'Milligrams':
        calculate = number1*28350
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Ounce' and result_to == 'Centigrams':
        calculate = number1*2835
        result.cget('text')
        result.configure(text = (calculate,result_to))
    
    elif result_from == 'Ounce' and result_to == 'Grams':
        calculate = number1*28.35
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Ounce' and result_to == 'Decigrams':
        calculate = number1*283.5
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Ounce' and result_to == 'Kilograms':
        calculate = number1/35.274
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Ounce' and result_to == 'Metric ton':
        calculate = number1/35270
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Ounce' and result_to == 'U.S. ton':
        calculate = number1/32000
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Ounce' and result_to == 'Imperial ton':
        calculate = number1/35840
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Ounce' and result_to == 'Pound':
        calculate = number1/16
        result.cget('text')
        result.configure(text = (calculate,result_to))

    elif result_from == 'Ounce' and result_to == 'Ounce':
        calculate = number1
        result.cget('text')
        result.configure(text = (calculate,result_to))

   
# Selected function
def selected(event):
    unit = event.widget.get()
    if unit == 'Volume':
        fromdd['values'] = ('Cubic meters',
                            'Cubic foot',
                            'Liters',
                            'U.S. Gallon',
                            'Cubic centimeters',
                            'U.S. Cup',
                            'Imperial Cup',
                            'Imperial Gallon')

        todd['values'] = ('Cubic meters',
                          'Cubic foot',
                          'Liters',
                          'U.S. Gallon',
                          'Cubic centimeters',
                          'U.S. Cup',
                          'Imperial Cup',
                          'Imperial Gallon')

    elif unit == 'Length':
        fromdd['values'] = ('Millimeters',
                            'Centimeters',
                            'Decimeters',
                            'Meters',
                            'Kilometers',
                            'Mile',
                            'Foot',
                            'Yard',
                            'Inch')

        todd['values'] = ('Millimeters',
                          'Centimeters',
                          'Decimeters',
                          'Meters',
                          'Kilometers',
                          'Mile',
                          'Foot',
                          'Yard',
                          'Inch')

    elif unit == 'Mass':
        fromdd['values'] = ('Milligrams',
                            'Centigrams',
                            'Grams',
                            'Decigrams',
                            'Kilograms',
                            'Metric ton',
                            'U.S. ton',
                            'Imperial ton',
                            'Pound',
                            'Ounce')

        todd['values'] = ('Milligrams',
                          'Centigrams',
                          'Grams',
                          'Decigrams',
                          'Kilograms',
                          'Metric ton',
                          'U.S. ton',
                          'Imperial ton',
                          'Pound',
                          'Ounce')
    


# Creating the unit converter label
main = tk.Label(window,text = 'Measurement Converter',bg = 'gray',fg = 'white', borderwidth=5, relief= 'raised')
main['font'] = font1
main.place(relx = '0.5',rely = '0.12',anchor = 'center')

# Creating the unit label
unit = tk.Label(window,text = 'Unit:',bg = 'gray', fg='white')
unit['font'] = font2
unit.place(relx = '0.5',rely = '0.258', anchor = 'center')

# Creating the main combobox
n = StringVar()
unitdd = ttk.Combobox(window,width = '7',textvariable = n)

# Values
unitdd['values'] = ('Volume',
                    'Length',
                    'Mass')

unitdd.place(relx = '0.5',rely = '0.3',anchor = 'center')
unitdd.current()
unitdd.bind('<<ComboboxSelected>>',selected)

# Creating the from label
label_from = tk.Label(window,text = 'From:',bg = 'gray', fg='white')
label_from['font'] = font2
label_from.place(relx='0.25',rely = '0.34')

# Creating the fromdd
f = StringVar()
fromdd = ttk.Combobox(window,width = '10',textvariable = f)

fromdd.place(relx = '0.3',rely = '0.4',anchor = 'center')
fromdd.current()
fromdd.bind('<<ComboboxSelected>>',fromfunc)

# Creating the num_from entry
num_from = tk.Entry(window,width = 10,textvariable = number_from)
num_from.place(relx = '0.37',rely = '0.49')

answer = partial(answer,num_from)

# Creating the entry label
label_from = tk.Label(window,text = 'Enter your number here:',bg = 'gray', fg='white')
label_from['font'] = font2
label_from.place(relx='0.356',rely = '0.46')

# Creating the to label
to = tk.Label(window,text = 'To:',bg = 'gray', fg='white')
to['font'] = font2
to.place(relx = '0.66',rely = '0.34')

# Creating arrow
arrow = tk.Label(window,text = '------->',bg = 'gray', fg='white')
arrow['font'] = font4
arrow.place(relx = '0.45',rely = '0.38')

# Creating the to drop down
t = StringVar()
todd = ttk.Combobox(window,width = 10,textvariable = t)

todd.place(relx = '0.7',rely = '0.4',anchor = 'center')
todd.current()
todd.bind('<<ComboboxSelected>>',tofunc)

# Creating the result box
result = tk.Label(window,text = '',bg= 'white',width = 30)
result['font'] = font3
result.place(relx = '0.5',rely = '0.7',anchor = 'center')

# Creating the result label
label_from = tk.Label(window,text = 'Result',bg = 'gray', fg='white')
label_from['font'] = font2
label_from.place(relx = '0.45',rely = '0.73')

# Creating the get answer button
get_answer = tk.Button(window,text = 'Convert',bg = 'cyan2',command = answer)
get_answer['font'] = font2
get_answer.place(relx = '0.5',rely = '0.6', anchor = 'center')

# Creating the mainloop
window.mainloop()
