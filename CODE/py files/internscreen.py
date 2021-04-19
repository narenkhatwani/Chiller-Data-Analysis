from tkinter import *
from tkinter import messagebox
import re, pymysql
# This function is used for adjusting window size and making the necessary configuration on start of window
global screen
def adjustWindow(window):
    
    global screen
    w = 600 # width for the window size
    h = 600 # height for the window size
    ws = screen.winfo_screenwidth() # width of the screen
    hs = screen.winfo_screenheight() # height of the screen
    x = (ws/2) - (w/2) # calculate x and y coordinates for the Tk window
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y)) # set the dimensions of the screen and where it is placed
    window.resizable(False, False) # disabling the resize option for the window
    window.configure(background='white') # making the background white of the window
    Label(screen, text="Enter New Record", width='31', height="2", font=("Calibri", 22, 'bold'), fg='white', bg='#d9660a').grid(row=0, sticky=W, columnspan=4)
    Button(screen, text='Submit', width=20, font=("Open Sans", 13, 'bold'), bg='brown', fg='white')
    
adjustWindow(screen)
screen.mainloop()














