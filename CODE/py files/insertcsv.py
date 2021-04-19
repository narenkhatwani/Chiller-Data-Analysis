from tkinter import *
from tkinter import messagebox
import re,pymysql
from tkinter import Tk
from tkinter import Label
from PIL import ImageTk, Image
from tkinter import *
from tkinter import messagebox
import re,pymysql
from tkinter import Tk
from PIL import ImageTk, Image
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from openpyxl import *
import numpy as np
import time
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


data_naren=pd.read_csv("C:\\Datasets\\internshipdataset1.csv")
data_harsh=pd.read_csv("C:\\Datasets\\internshipdataset1.csv")
data_priya=pd.read_csv("C:\\Datasets\\Dataset2.csv")#reading csv file

#data_naren= data_naren[np.isfinite(data_naren['Installs'])]

def adjustWindow(window): 
    w = 800  # width for the window size 
    h = 800  # height for the window size 
    ws = screen.winfo_screenwidth()  # width of the screen 
    hs = screen.winfo_screenheight()  # height of the screen 
    x = (ws/2) - (w/2)  # calculate x and y coordinates for the Tk window 
    y = (hs/2) - (h/2) 
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))  # set the dimensions of the screen and where it is placed 
    window.resizable(True,True)    # disabling the resize option for the window 
    window.configure(background='white')
    
    
def main_screen():
    global screen,a
    screen = Tk()
   
    screen.title("BRUTE FORCE")
    adjustWindow(screen)
    variable = StringVar(screen)
    variable.set("Category") # default value

    w = OptionMenu(screen,variable,"Category", "FAMILY", "COMMUNICATION")
    w.pack()
    
    
    a=variable.get()
    Button(screen, text='Submit', width=20, font=("Open Sans", 13, 'bold'), bg='brown', fg='black',command=quater_cat).pack()
    
    
    screen.mainloop()
        
def function2():
    global screen4,a 
    screen4 = Toplevel(screen) 
    screen4.title("FUNCTION 2")
    adjustWindow(screen4)



    plt.subplots(figsize=(7,7))
    plt.title("THE PERCENTAGE OF DOWNLOADS CATEGORY WISE")
    sns.countplot(y=data_naren[a])
    plt.yticks(fontsize=7)
    plt.savefig('C:\\Users\\Admin\\Desktop\\internship gui\\function1.jpg',dpi=100)
    
    
    img = ImageTk.PhotoImage(Image.open('function1.jpg'))
    panel =Label(screen4, image = img)
    panel.pack()    
    #panel.place(x=30,y=-50)
    screen4.mainloop()
    

'''    
def function1():
    global screen4,a 
    screen4 = Toplevel(screen) 
    screen4.title("FUNCTION 1")
    adjustWindow(screen4)



    plt.subplots(figsize=(7,7))
    plt.title("THE PERCENTAGE OF DOWNLOADS CATEGORY WISE")
    sns.countplot(y=data_naren[a])
    plt.yticks(fontsize=7)
    plt.savefig('C:\\Users\\Admin\\Desktop\\internship gui\\function1.jpg',dpi=100)
    
    
    img = ImageTk.PhotoImage(Image.open('function1.jpg'))
    panel =Label(screen4, image = img)
    panel.pack()    
    #panel.place(x=30,y=-50)
    screen4.mainloop()    

'''




main_screen()





















