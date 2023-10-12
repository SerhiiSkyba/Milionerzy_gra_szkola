import os
import sys

if sys.argv:
    filepath = sys.argv[0]
    folder, filename = os.path.split(filepath)
    os.chdir(folder) # now your working dir is the parent folder of the script
import customtkinter as ctk
from tkinter import *

windowstart=ctk.CTk()
bg = PhotoImage(file = "milioner2.png")
windowstart.resizable(False,False)
windowstart.geometry("560x500")
windowstart.title("Gra Milionerzy")
font_default = ("Inter",16,'normal')
font_pytanie = ("Inter",16,'bold')
font_color='#121212'
width=25
height=1

def start():
    windowstart.destroy()
    from Main import windowgra
   

def quit():
    windowstart.destroy()

limg= Label(windowstart, i=bg)
frame = ctk.CTkFrame(windowstart)
Start = ctk.CTkButton(frame,
                 text="rozpocznij grę",
                 font=font_default,
                 corner_radius=0,
                 command=lambda: start())
Quit = ctk.CTkButton(frame,
                 text="wyjdź",
                 font=font_default,
                 corner_radius=0,
                 command=lambda: quit())


Quit.pack(side=LEFT, expand = True, fill = BOTH)
Start.pack(side=LEFT, expand = True, fill = BOTH)
frame.pack(side = BOTTOM,expand = True, fill = BOTH)

limg.pack()

windowstart.mainloop()
