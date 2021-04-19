from tkinter import *
from tkinter import messagebox
import re,pymysql
from tkinter import Tk
from PIL import ImageTk, Image
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates
from seaborn import regplot
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder
from openpyxl import *
from tkinter import *
from tkinter import messagebox
import re , pymysql
from tkinter import Tk
from PIL import ImageTk, Image 
from matplotlib.pyplot import title
from matplotlib.pyplot import subplots
from matplotlib.pyplot import subplot
from numpy import array
from numpy import mean
from numpy import nan
from pandas import read_csv
from pandas import to_numeric
from pandas import notnull
from fractions import Fraction
from matplotlib.pyplot import bar
from matplotlib.pyplot import ylim
from matplotlib.pyplot import xlabel
from matplotlib.pyplot import ylabel
from matplotlib.pyplot import title
from matplotlib.pyplot import xticks
from matplotlib.pyplot import subplots
from matplotlib.pyplot import subplot
from matplotlib.pyplot import show
from matplotlib.pyplot import scatter
from matplotlib.pyplot import plot
from matplotlib.pyplot import tight_layout
from seaborn import barplot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import BOTH
from tkinter import BOTTOM
from tkinter import TOP
from tkinter import Text
from tkinter import END
from tkinter import Label
from tkinter import Scrollbar
from tkinter import messagebox
from tkinter import W
from tkinter import Entry
from csv import writer
from PIL import ImageTk, Image


data_naren=pd.read_csv("Internship-project-Dataset1 (1).csv")
data_naren= data_naren[notnull(data_naren['Rating'])]
#data_harsh=pd.read_csv("C:\\Datasets\\internshipdataset1.csv")
data_priya=pd.read_csv("Internship-project-Dataset2.csv")


data_naren = data_naren.drop_duplicates()
data_naren.drop(data_naren[data_naren['Installs'] == 'Free'].index, inplace = True)
data_naren.drop(data_naren[data_naren['Category'] == '1.9'].index, inplace = True)
data_naren['Size'] = data_naren['Size'].apply(lambda x: str(float(x.replace('k', '')) / 1000) if 'k' in x else x)
data_naren['Size'] = data_naren['Size'].replace('Varies with device', nan)
chars_to_remove = ['+', ',', 'M', '$']
cols_to_clean = ['Installs', 'Size', 'Price']
data_naren['Installs']=data_naren['Installs'].map(lambda x:x.rstrip('+'))
data_naren['Installs']=data_naren['Installs'].map(lambda x:''.join(x.split(',')))

data_naren= data_naren[notnull(data_naren['Rating'])]
data_naren= data_naren[notnull(data_naren['Size'])]
data_naren = data_naren[notnull(data_naren['Android Ver'])]
         
        
data_priya = data_priya[notnull(data_priya['Translated_Review'])]
data_priya = data_priya[notnull(data_priya['Sentiment'])]
data_priya= data_priya[notnull(data_priya['Sentiment_Polarity'])]
data_priya= data_priya[notnull(data_priya['Sentiment_Subjectivity'])]

data_naren.dropna(axis=1)


data_naren['Installs']=data_naren['Installs'].map(lambda x:x.rstrip('+'))
data_naren['Installs']=data_naren['Installs'].map(lambda x:''.join(x.split(',')))

data_naren['Year'] = pd.DatetimeIndex(data_naren['Last Updated']).year
# This function is used for adjusting window size and making the necessary configuration on start of window 
def adjustWindow(window): 
    w = 800  # width for the window size 
    h = 600  # height for the window size 
    ws = screen.winfo_screenwidth()  # width of the screen 
    hs = screen.winfo_screenheight()  # height of the screen 
    x = (ws/2) - (w/2)  # calculate x and y coordinates for the Tk window 
    y = (hs/2) - (h/2) 
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))  # set the dimensions of the screen and where it is placed 
    window.resizable(False, False)    # disabling the resize option for the window 
    window.configure(background='white')    # making the background white of the window


# This function is used for adjusting window size and making the necessary configuration on start of window 
def adjustWindow1(window): 
    w = screen.winfo_screenwidth()  # width of the screen 
    h = screen.winfo_screenheight()  # height of the screen 
    x = (w/2)  # calculate x and y coordinates for the Tk window 
    y = (h/2) 
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))  # set the dimensions of the screen and where it is placed 
    #window.resizable(False, False)    # disabling the resize option for the window 
    window.configure(background='white')    # making the background white of the window

def adjustWindow2(window): 
    w = 900
    h = 750
    ws = welcome_screen.winfo_screenwidth()
    hs = welcome_screen.winfo_screenheight()
    x = (ws/3.5) - (w/3.5)
    y = (hs/3.5) - (h/3.5) 
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    window.resizable(False, False)
# registration window 
def register(): 
    global screen1, fullname, email, password, repassword, country, gender, tnc # making all entry field variable global 
    fullname = StringVar() 
    email = StringVar() 
    password = StringVar() 
    repassword = StringVar() 
    gender = StringVar() 
    country = IntVar() 
    tnc = IntVar() 
    screen1 = Toplevel(screen) 
    screen1.title("BRUTE FORCE") 
    adjustWindow(screen1) # configuring the window 
    Label(screen1, text="Registration Form", width='55', height="2", font=("Calibri", 22, 'bold'), fg='#d9660a').place(x=0, y=0)
    #Label(screen1, text="", bg='#174873', width='55', height='30').place(x=105, y=100) 
    
    photo = PhotoImage(file="reg.png") # opening left side image - Note: If image is in same folder then no need to mention the full path 
    label = Label(screen1, image=photo, text="") # attaching image to the label 
    label.place(x=-1, y=80) 
    label.image = photo # it is necessary in Tkinter to keep a instance of image to display image in label 

   
    #Label(screen1, text="REGISTRATION FORM", font=("Open Sans", 22, 'bold'), fg='white', bg='#174873', anchor=W).place(x=250, y=30) 
    #Label(screen1, text="Registration Form", width='55', height="1", font=("Calibri", 22, 'bold'), fg='#d9660a').place(x=0, y=20) 
    Label(screen1, text="Full Name:", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=350, y=130) 
    Entry(screen1, textvar=fullname).place(x=480, y=130) 
    Label(screen1, text="Email ID:", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=350, y=180) 
    Entry(screen1, textvar=email).place(x=480, y=180) 
    Label(screen1, text="Country:", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=350, y=230) 
    Radiobutton(screen1, text="India", variable=country, value=1,fg='white', bg='#174873').place(x=480, y=230)     
    Radiobutton(screen1, text="Other", variable=country, value=2,fg='white', bg='#174873').place(x=550, y=230) 
                    
    Label(screen1, text="gender:", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=350, y=280) 
    list1 = ['Male','Female','Other']
    droplist = OptionMenu(screen1, gender, *list1) 
    droplist.config(width=18) 
    gender.set('--select your gender--') 
    droplist.place(x=480, y=275) 
    Label(screen1, text="Password:", font=("Open Sans", 11, 'bold'), fg='white',bg='#174873', anchor=W).place(x=350, y=330) 
    Entry(screen1, textvar=password, show="*").place(x=480, y=330) 
    Label(screen1, text="Re-Password:", font=("Open Sans", 11, 'bold'), fg='white',bg='#174873', anchor=W).place(x=350, y=380) 
    entry_4 = Entry(screen1, textvar=repassword, show="*") 
    entry_4.place(x=480, y=380) 
    Checkbutton(screen1, text="I accept all terms and conditions", variable=tnc, font=("Open Sans", 9, 'bold'), fg='brown').place(x=375, y=430) 
    Button(screen1, text='Submit', width=15, font=("Open Sans", 13, 'bold'), bg='brown', fg='black',command=register_user).place(x=330, y=480)              
    Button(screen1, text='Back', width=10, font=("Open Sans", 13, 'bold'), bg='brown', fg='black',command=screen1.destroy).place(x=550, y=480)              

    photo = PhotoImage(file="log.png") # opening left side image - Note: If image is in same folder then no need to mention the full path 
    label = Label(screen1, image=photo, text="") # attaching image to the label 
    label.place(x=130, y=0) 
    label.image = photo # it is necessary in Tkinter to keep a instance of image to display image in label 
    
         

def register_user(): 
    if fullname.get() and email.get() and password.get() and repassword.get() and country.get(): # checking for all empty values in entry field 
        if gender.get() == "--select your gender--": # checking for selection of university 
            Label(screen1, text="Please select your gender", fg="red", 
                  font=("calibri", 11), width='30', anchor=W, bg='white').place(x=0, y=570) 
            return 
        else: 
            if tnc.get(): # checking for acceptance of agreement 
                if re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email.get()): # validating the email 
                    if password.get() == repassword.get(): # checking both password match or not 
                        # if u enter in this block everything is fine just enter the values in database 
                        country_value = 'India' 
                        if country.get() == 2:  
                            
                            country_value = 'Other' 
                        connection = pymysql.connect(host="localhost", user="root", passwd="", database="bruteforce") # database connection 
                        cursor = connection.cursor() 
                        insert_query = "INSERT INTO registration_details (fullname, email, password, country,gender) VALUES('"+ fullname.get() + "', '"+ email.get() + "', '"+ password.get() + "', '"+ country_value + "', '"+ gender.get() + "' );" # queries for inserting values 
                        cursor.execute(insert_query) # executing the queries 
                        connection.commit() # commiting the connection then closing it. 
                        connection.close() # closing the connection of the database 
                        Label(screen1, text="Registration Sucess", fg="green", font=( "calibri", 11), width='30', anchor=W, bg='white').place(x=0, y=570) # printing successful registration message 
                        Button(screen1, text='Proceed to Login ->', width=20, font=("Open Sans", 9, 'bold'), bg='brown', fg='white',command=screen1.destroy).place(x=170, y=565) # button to navigate back to login page 
                    else: 
                        Label(screen1, text="Password does not match", fg="red", font=( "calibri", 11), width='30', anchor=W, bg='white').place(x=0, y=570) 
                        return 
                else: 
                    Label(screen1, text="Please enter valid email id", fg="red", font=("calibri", 11), width='30', anchor=W, bg='white').place(x=0, y=570) 
                    return 
            else: 
                Label(screen1, text="Please accept the agreement", fg="red", 
                      font=("calibri", 11), width='30', anchor=W, bg='white').place(x=0, y=570) 
                return 
    else: 
        Label(screen1, text="Please fill all the details", fg="red", 
        font=("calibri", 11), width='30', anchor=W, bg='white').place(x=0, y=570) 
        return 

# login creditentials verification 
def login_verify(): 
    global registrationID 
    connection = pymysql.connect(host="localhost", user="root", passwd="", database="bruteforce") # database connection 
    cursor = connection.cursor() 
    select_query =  "SELECT * FROM registration_details where email = '" + username_verify.get() + "' AND password = '" + password_verify.get() + "';" # queries for retrieving values 
    cursor.execute(select_query) # executing the queries 
    registration_info = cursor.fetchall() 
    connection.commit() # commiting the connection then closing it. 
    connection.close() # closing the connection of the database                     
    if registration_info: 
        messagebox.showinfo("Congratulation", "Login Succesfull") # displaying message for successful login 
        registrationID = registration_info[0][0] 
        welcome_page(registration_info) # opening welcome window 
    else: 
        messagebox.showerror("Error", "Invalid Username or Password") # displaying message for invalid details 


# welcome window 
def welcome_page(registration_info): 
    global screen2 
    screen2 = Toplevel(screen) 
    screen2.title("BRUTE FORCE") 
    adjustWindow(screen2) # configuring the window 
    Label(screen2, text="Welcome " + registration_info[0][1], width='47', height="2", font=("Calibri", 25, 'bold'), fg='white', bg='#d9660a').place(x=0, y=0) 
    Label(screen2, text="", bg='#174873', width='20', height='20').place(x=0, y=96) 
    Message(screen2, text='“If we have data, let’s look at data. If all we have are opinions, let’s go with mine.”\n\n - — Jim Barksdale', width='100', font=("Helvetica", 10, 'bold', 'italic'), fg='white', bg='#174873', anchor = CENTER).place(x=10, y=100) 
    
    #photo = PhotoImage(file="bft.png") # opening left side image - Note: If image is in same folder then no need to mention the full path 
    #label = Label(screen2, image=photo, text="") # attaching image to the label 
    #label.place(x=10, y=270) 
    #label.image = photo # it is necessary in Tkinter to keep a instance of image to display image in label 
    
    photo1 = PhotoImage(file="analy.png") # opening right side image - Note: If image is in same folder then no need to mention the full path 
    label1 = Label(screen2, image=photo1, text="") # attaching image to the label 
    label1.place(x=150, y=96) 
    label1.image = photo1 # it is necessary in Tkinter to keep a instance of image to display image in label 
    
    photo1 = PhotoImage(file="pay.png") # opening right side image - Note: If image is in same folder then no need to mention the full path 
    label1 = Label(screen2, image=photo1, text="") # attaching image to the label 
    label1.place(x=180, y=0) 
    label1.image = photo1 # it is necessary in Tkinter to keep a instance of image to display image in label 
  
    
    Button(screen2, text='Fetch Record', width=20,height=4, font=("Open Sans", 13, 'bold'), bg='brown', fg='white').place(x=270, y=150) 
    Button(screen2, text='Insert Record', width=20,height=4, font=("Open Sans", 13, 'bold'), bg='brown', fg='white').place(x=270, y=250) 
    Button(screen2, text='Perform Function', width=20,height=4, font=("Open Sans", 13, 'bold'), bg='brown', fg='white',command=next_page).place(x=270, y=350)
    Button(screen2, text='Back', width=10, font=("Open Sans", 13, 'bold'), bg='brown', fg='black',command=screen2.destroy).place(x=380, y=500)              

    
def next_page():    
    global screen3 
    screen3 = Toplevel(screen) 
    screen3.title("BRUTE FORCE")
    #adjustWindow(screen3)
    screen3.geometry("950x650")
    screen3.resizable(False,False)

    photo1 = PhotoImage(file="smok1.png") # opening right side image - Note: If image is in same folder then no need to mention the full path 
    label1 = Label(screen3, image=photo1, text="") # attaching image to the label 
    label1.place(x=-5, y=50) 
    label1.image = photo1 # it is necessary in Tkinter to keep a instance of image to display image in label 
                
    Label(screen3, text="--Functions-- ",width=40, height=1, font=("Open Sans", 30, 'bold'), bg='#174873', fg='white').place(x=0,y=0)             

    Label(screen3, text="Page 1/3 ",width=8, height=1, font=("Open Sans", 13, 'bold'), fg='black', bg='white').place(x=400,y=600)             

    #Button(screen3, text='Function 1', width=15, height=1,font=("Open Sans", 15, 'bold'), bg='brown', fg='black').place(x=800, y=100)              
    Button(screen3, text="1) What is the percentage download in each category on the playstore.",width=70, height=2, bg='brown', fg='white',font=("Open Sans", 10, 'bold'),command=question_1).place(x=80,y=84)
    #Button(screen3, text='Function 2', width=15, height=1,font=("Open Sans", 15, 'bold'), bg='brown', fg='black').place(x=800, y=175)              
    Button(screen3, text="""2) How many apps have managed to get the following number of downloads a) Between 10,000 and 50,000         
    b) Between 50,000 and 150000 c) Between 150000 and 500000 d) Between 500000 and 5000000 e) More than 5000000""",width=95, height=2, bg='brown', fg='white',command=question_2,font=("Open Sans", 10, 'bold')).place(x=80,y=166)
    #Button(screen3, text='3', width=1, height=1,font=("Open Sans", 15, 'bold'), bg='brown', fg='black').place(x=30, y=250)              
    Button(screen3, text="3) Which category of apps have managed to get the most,least and an average of 2,50,000 downloads atleast.",width=90, height=2,font=("Open Sans", 10, 'bold'), bg='brown', fg='white',command=question_3).place(x=80,y=248)
    Button(screen3, text="4) Which category of apps have managed to get the highest maximum average ratings from the users.",width=90, height=2,font=("Open Sans", 10, 'bold'), bg='brown', fg='white',command=question_4).place(x=80,y=332)
    Button(screen3, text="5) What is the download trend category wise over the period for which the data is being made available.",width=90, height=2,font=("Open Sans", 10, 'bold'), bg='brown', fg='white',command=question_5).place(x=80,y=416)
    Button(screen3, text="""6) For the years 2016,2017,2018 what are the category of apps that have got the most and the least downloads.
     What is the percentage increase or decrease that the apps have got over the period of three years""",width=90, height=2,font=("Open Sans", 10, 'bold'), bg='brown', fg='white',command=function6).place(x=80,y=500)
    
    Button(screen3, text='< Back', width=10, font=("Open Sans", 13, 'bold'), bg='brown', fg='black',command=screen3.destroy).place(x=40, y=590)              
    Button(screen3, text='Next >', width=10, font=("Open Sans", 13, 'bold'), bg='brown', fg='black',command=next_page1).place(x=800, y=590)              


def next_page1():    
    global screen311 
    screen311 = Toplevel(screen) 
    screen311.title("BRUTE FORCE")
    #adjustWindow(screen311)
    screen311.geometry("950x650")
    screen311.resizable(False,False)

    photo1 = PhotoImage(file="smok1.png") # opening right side image - Note: If image is in same folder then no need to mention the full path 
    label1 = Label(screen311, image=photo1, text="") # attaching image to the label 
    label1.place(x=-5, y=50) 
    label1.image = photo1 # it is necessary in Tkinter to keep a instance of image to display image in label 
                
    Label(screen311, text="--Functions-- ",width=40, height=1, font=("Open Sans", 30, 'bold'), bg='#174873', fg='white').place(x=0,y=0)             

    Label(screen311, text="Page 2/3 ",width=8, height=1, font=("Open Sans", 13, 'bold'), fg='black', bg='white').place(x=400,y=600)             

    
    Button(screen311, text="""7) All those apps , whose android version is not an issue and can work with varying devices ,
     what is the percentage increase or decrease in the downloads.""",width=90, height=2,font=("Open Sans", 10, 'bold'), bg='brown', fg='white',command=function7).place(x=80,y=84)
    
    Button(screen311, text="""8) Amongst sports, entertainment,social media,news,events,travel and games,which is the category of app that is
    most likely to be downloaded in the coming years, kindly make a prediction and back it with suitable findings.""",width=95, height=2, bg='brown', fg='white',font=("Open Sans", 10, 'bold'),command=question_8).place(x=80,y=164)
    Button(screen311, text="""9) All those apps who habve managed to get over 1,00,000 downloads, have they managed to get an average rating
    of 4.1 and above? An we conclude something in co-relation to the number of downloads and the ratings received.""",width=95, height=2, bg='brown', fg='white',font=("Open Sans", 10, 'bold'),command=function9).place(x=80,y=248)
    Button(screen311, text="""10) Across all the years ,which month has seen the maximum downloads fr each of the category. 
    What is the ratio of downloads for the app that qualifies as teen versus mature17+""",width=90, height=2,font=("Open Sans", 10, 'bold'), bg='brown', fg='white',command=question_10).place(x=80,y=332)
    Button(screen311, text="11) Which quarter of which year has generated the highest number of install for each app used in the study?",width=90, height=2,font=("Open Sans", 10, 'bold'), bg='brown', fg='white',command=question_11).place(x=80,y=416)
    Button(screen311, text="""12) Which of all the apps given have managed to generate the most positive and negative sentiments.Also figure 
    out the app which has generated approximately the same ratio for positive and negative sentiments.""",width=90, height=2,font=("Open Sans", 10, 'bold'), bg='brown', fg='white',command=question_12).place(x=80,y=500)
    
    
    #Button(screen311, text="13) Study and find out the relation between the Sentiment-polarity and sentiment-subjectivity of all the apps.",width=90, height=2,font=("Open Sans", 10, 'bold'), bg='brown', fg='white').place(x=80,y=430)
    #Button(screen311, text="""14) Generate an interface where the client can see the reviews categorized as positive.negative and neutral 
    #,once they have selected the app from a list of apps available for the study.""",width=90, height=2,font=("Open Sans", 10, 'bold'), bg='brown', fg='white').place(x=80,y=500)
    
    Button(screen311, text='< Back', width=10, font=("Open Sans", 13, 'bold'), bg='brown', fg='black',command=screen311.destroy).place(x=40, y=590)              
    Button(screen311, text='Next >', width=10, font=("Open Sans", 13, 'bold'), bg='brown', fg='black',command=next_page2).place(x=800, y=590)              

def next_page2():    
    global screen312 
    screen312 = Toplevel(screen) 
    screen312.title("BRUTE FORCE")
    #adjustWindow(screen312)
    screen312.geometry("950x650")
    screen312.resizable(False,False)

    photo1 = PhotoImage(file="smok1.png") # opening right side image - Note: If image is in same folder then no need to mention the full path 
    label1 = Label(screen312, image=photo1, text="") # attaching image to the label 
    label1.place(x=-5, y=50) 
    label1.image = photo1 # it is necessary in Tkinter to keep a instance of image to display image in label 
                
    Label(screen312, text="--Functions-- ",width=40, height=1, font=("Open Sans", 30, 'bold'), bg='#174873', fg='white').place(x=0,y=0)             

    Label(screen312, text="Page 3/3 ",width=8, height=1, font=("Open Sans", 13, 'bold'), fg='black', bg='white').place(x=400,y=600)             

    
    Button(screen312, text="13) Study and find out the relation between the Sentiment-polarity and sentiment-subjectivity of all the apps.",width=90, height=2,font=("Open Sans", 10, 'bold'), bg='brown', fg='white',command=question_13).place(x=80,y=84)
    Button(screen312, text="""14) Generate an interface where the client can see the reviews categorized as positive.negative and neutral 
    ,once they have selected the app from a list of apps available for the study.""",width=90, height=2,font=("Open Sans", 10, 'bold'), bg='brown', fg='white',command=question_14).place(x=80,y=164)
    
    Button(screen312, text="15) Is it advisable to launch an app like ’10 Best foods for you’? Do the users like these apps?",width=95, height=2, bg='brown', fg='white',command=question_15,font=("Open Sans", 10, 'bold')).place(x=80,y=248)
    Button(screen312, text="16) Which month(s) of the year, is the best indicator to the avarage downloads that an app will generate over the entire year?",width=90, height=2,font=("Open Sans", 10, 'bold'), bg='brown', fg='white',command=question_16).place(x=80,y=332)
    Button(screen312, text="""17) Does the size of the App influence the number of installs that it gets ? 
    if,yes the trend is positive or negative with the increase in the app size.""",width=90, height=2,font=("Open Sans", 10, 'bold'), bg='brown', fg='white',command=question_17).place(x=80,y=416)
    Button(screen312, text="18) Provide an interface to add new data to both the datasets provided.",width=90, height=2,font=("Open Sans", 10, 'bold'), bg='brown', fg='white',command=question_18_first_page).place(x=80,y=500)
    
    
        
    Button(screen312, text='< Back', width=10, font=("Open Sans", 13, 'bold'), bg='brown', fg='black',command=screen312.destroy).place(x=40, y=590)              
    #Button(screen312, text='Next >', width=10, font=("Open Sans", 13, 'bold'), bg='brown', fg='black').place(x=800, y=590)              




def main_screen():
    global screen, username_verify, password_verify
    screen = Tk()
    username_verify = StringVar()
    password_verify = StringVar()
    screen.title("BRUTE FORCE")
    adjustWindow(screen)
    
    img2 = ImageTk.PhotoImage(Image.open("bigdata.png"))  
    d1 = Label(image= img2) 
    d1.place(x =-1,y = 78)
    
    Label(screen,text="BRUTE FORCE Manager",width="55",height="2",font=("Calibri",22,'bold'),bg='white',fg='#174873').pack()
    Label(screen, text="Please enter details below to login", bg='#174873', fg='white').place(x=312,y=150) 
    Label(screen, text="Username * ", font=("Open Sans", 10, 'bold'), bg='#174873', fg='white').place(x=358,y=192)             
    Entry(screen, textvar=username_verify).place(x=337,y=215) 
    Label(screen, text="Password * ", font=("Open Sans", 10, 'bold'), bg='#174873', fg='white').place(x=358,y=262) 
    Entry(screen, textvar=password_verify, show="*").place(x=337,y=285) 
    Button(screen, text="LOGIN", bg="#e79700", width=15, height=1, font=("Open Sans", 13, 'bold'), fg='white', command=login_verify).place(x=320,y=325) 
    Button(screen, text="New User? Register Here", height="2", width="30", bg='#e79700', font=("Open Sans", 10, 'bold'), fg='white', command=register).place(x=270,y=380) 
    
    img1 = ImageTk.PhotoImage(Image.open("bft.png"))  
    c1 = Label(image= img1) 
    c1.place(x =142,y = 0) 
    
    
           
    screen.mainloop()
    
def function1():
    global screen4 
    screen4 = Toplevel(screen) 
    screen4.title("FUNCTION 1")
    adjustWindow(screen4)

    plt.subplots(figsize=(6,6))
    plt.title("THE PERCENTAGE OF DOWNLOADS CATEGORY WISE")
    sns.countplot(data_naren['Category'],label='percentage')
    plt.xticks(fontsize=7,rotation=90)
    plt.savefig('C:\\Users\\Admin\\Desktop\\internship gui\\function1.jpg',dpi=100)  
    
    img = ImageTk.PhotoImage(Image.open('C:\\Users\\Admin\\Desktop\\internship gui\\.function1.png'))
    panel =Label(screen4, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")
        
    screen4.mainloop()


#function2
def function2():
    global screen5 
    screen5 = Toplevel(screen) 
    screen5.title("FUNCTION 2")
    adjustWindow(screen5)
    
    data_naren['Installs']=data_naren['Installs'].map(lambda x:x.rstrip('+'))
    data_naren['Installs']=data_naren['Installs'].map(lambda x:''.join(x.split(',')))
    
    #10,000 to 50,000
    x1=data_naren.loc[(data_naren['Installs']=='10000'),['Installs','App']].count() 
    y1=data_naren.loc[(data_naren['Installs']=='50000'),['Installs','App']].count() 
    
    Label(screen5, text="The app downloads 10,000 to 50,000:", fg='black').pack()
    Label(screen5, text=x1+y1, bg='yellow', fg='black').pack()
    
    
        
    #50,000 to 150,000
    x2=data_naren.loc[(data_naren['Installs']=='50000'),['Installs','App']].count() 
    y2=data_naren.loc[(data_naren['Installs']=='150000'),['Installs','App']].count() 
    
    Label(screen5, text="The app downloads 50,000 to 150,000:", fg='black').pack()
    Label(screen5, text=x2+y2, bg='yellow', fg='black').pack()
    
    #50,000 to 150,000 ends here
    
    
    #150000 to 500000
    x3=data_naren.loc[(data_naren['Installs']=='150000'),['Installs','App']].count() 
    y3=data_naren.loc[(data_naren['Installs']=='500000'),['Installs','App']].count() 
    
    Label(screen5, text="The app downloads 150000 to 500000:", fg='black').pack()
    Label(screen5, text=x3+y3, bg='yellow', fg='black').pack()
    #150000 to 500000 ends here
    
    #500000 to 
    x4=data_naren.loc[(data_naren['Installs']=='500000'),['Installs','App']].count() 
    y4=data_naren.loc[(data_naren['Installs']=='5000000'),['Installs','App']].count() 
    
    Label(screen5, text="The app downloads 500000 to :", fg='black').pack()
    Label(screen5, text=x4+y4, bg='yellow', fg='black').pack()
    #500000 to ends here
     
    #above 5000000
    y5=data_naren.loc[(data_naren['Installs']=='5000000'),['Installs','App']].count() 
    
    Label(screen5, text="The app downloads above 50 lakhs is:", fg='black').pack()
    Label(screen5, text=y5,fg='black').pack()
    

    screen5.mainloop()
 
    
#function5
def function11():
    global screen69,catname2,yearnum
    app_name=StringVar()
    screen69 = Toplevel(screen) 
    screen69.title("FUNCTION 14")
    #adjustWindow(screen24) 
    screen69.geometry("490x310")
    screen.resizable(False,False)
    data_naren['Year'] = pd.DatetimeIndex(data_naren['Last Updated']).year
    photo14 = PhotoImage(file="dark.png") # opening right side image - Note: If image is in same folder then no need to mention the full path 
    label14 = Label(screen69, image=photo14, text="") # attaching image to the label 
    label14.place(x=-12, y=-12) 
    label14.image = photo14 # it is necessary in Tkinter to keep a instance of image to display image in label 

    catname2= StringVar(screen69)
    catname2.set("drop down menu button")
    
    yearnum= IntVar(screen69)
    yearnum.set("drop down menu button")
    
    def grab_and_assign5(event):
        global chosen_option
        chosen_option1 = catname2.get() 
        label_chosen_variable= Label(screen69, text=chosen_option1)
        label_chosen_variable.pack()
    
    def grab_and_assign6(event):
        global chosen_option
        chosen_option2 = yearnum.get() 
        label_chosen_variable= Label(screen69, text=chosen_option2)
        label_chosen_variable.pack()
        
    drop_menu = OptionMenu(screen69,catname2,'ART_AND_DESIGN','AUTO_AND_VEHICLES','BEAUTY','BOOKS_AND_REFERENCE','BUSINESS','COMICS','COMMUNICATION','DATING','EDUCATION','ENTERTAINMENT','EVENTS','FINANCE','FOOD_AND_DRINK','HEALTH_AND_FITNESS','HOUSE_AND_HOME','LIBRARIES_AND_DEMO','LIFESTYLE','GAME','FAMILY','MEDICAL','SOCIAL','SHOPPING','PHOTOGRAPHY','SPORTS','TRAVEL_AND_LOCAL','TOOLS','PERSONALIZATION','PRODUCTIVITY','PARENTING','WEATHER','VIDEO_PLAYERS','NEWS_AND_MAGAZINES','MAPS_AND_NAVIGATION',command=grab_and_assign5)
    drop_menu.pack()#drop_menu.grid(row=0, column=0)
    
    drop_menu = OptionMenu(screen69,yearnum,'2011','2012','2013','2014','2015','2016','2017','2018',command=grab_and_assign6)
    drop_menu.pack()#drop_menu.grid(row=0, column=0)
    
           
    Button(screen69, text="Proceed", height="2", width="30",  bg='brown', font=("Open Sans", 10, 'bold'), fg='white', command=function11sub).place(x=120,y=220)
    
    screen69.mainloop()

def function11sub():
    global screen70,catname2,yearnum
    screen70 = Toplevel(screen) 
    screen70.title("FUNCTION 14")
    adjustWindow(screen70)
    #screen25.geometry("800x800")
    chosen_option1 = catname2.get()
    chosen_option2 = yearnum.get()
    data_naren['Year'] = pd.DatetimeIndex(data_naren['Last Updated']).year
    
    
    plt.subplots(figsize=(6,6))
    plt.title("THE PERCENTAGE OF DOWNLOADS CATEGORY WISE")
    sns.countplot(data_naren['Category']==chosen_option1,hue=data_naren['Year']==chosen_option2)
    plt.xticks(fontsize=6,rotation=78)
    plt.savefig('C:\\Users\\Admin\\Desktop\\internship gui\\function5.jpg',dpi=100)
    
    img = ImageTk.PhotoImage(Image.open('function5.jpg'))
    panel =Label(screen70, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")
    
    screen70.mainloop()


def question_3() :
    global screen3
    screen3 = Tk()
    screen3.title('Question-3')
    adjustWindow(screen3)
    category = data_naren['Category']
    installs = data_naren['Installs']
    category_list = []
    install_list = []
    cat_list = []
    required_count = []
    required_category = []
    required_count_2 = []
    sum_list = []
    for cat in category :
        if cat not in category_list :
            category_list.append(cat)
        cat_list.append(cat)
    for install in installs :
        if install == 'Free' :
            install_list.append(0)
        else :
            install_list.append(int(install))
    for cat in category_list :
        inst_count = 0
        for i in range(len(install_list)) :
            if cat == cat_list[i] and install_list[i] >= 250000:
                inst_count += 1
        required_count.append(inst_count)
    max_count = max(required_count)
    min_count = min(required_count)    
    for cat in category_list :
        dummy_sum = 0
        for i in range(len(cat_list)) :
            if cat_list[i] == cat :
                dummy_sum += install_list[i]
        sum_list.append(dummy_sum)
    for i in range(len(sum_list)) :
        if sum_list[i] >= 250000 :
            required_count_2.append(sum_list[i])
            required_category.append(category_list[i])
    max_count_2 = max(required_count_2)
    min_count_2 = min(required_count_2)    
    #set(style="darkgrid")
    f, ax = subplots(figsize=(9, 7))
    subplot(1,2,1)
    Label(screen3, text="Max count: {} of category {} ".format((max_count), category_list[required_count.index(max_count)]), font=("Open Sans", 15, 'bold'), fg='black').pack() 
    Label(screen3, text="Min count: {} of category {} ".format((min_count), category_list[required_count.index(min_count)], ), font=("Open Sans", 15, 'bold'), fg='black').pack() 
    title('Category vs Count', size=15)
    barplot(category_list, required_count).set(xlabel='Categories', ylabel='Count')
    xticks(rotation=90)
    subplot(1,2,2)
    Label(screen3, text="Maximum sum {} of category : {}".format(max_count_2, required_category[required_count_2.index(max_count_2)]), font=("Open Sans", 15, 'bold'), fg='black').pack() 
    Label(screen3, text="Minimum sum {} of category : {}".format(min_count_2, required_category[required_count_2.index(min_count_2)]), font=("Open Sans", 15, 'bold'), fg='black').pack() 
    title('Category vs Sum of installs', size=15)
    barplot(x=required_category, y=required_count_2).set(xlabel = 'Category', ylabel = 'Downloads')
    xticks(rotation=90)
    show()
    canvas = FigureCanvasTkAgg(f, screen3) 
    canvas.draw()
    canvas.get_tk_widget().pack(side = TOP, fill = BOTH, expand = True)    
    button = Button(screen3, text="Quit", command=screen3.destroy)
    button.pack(side=BOTTOM)
#


    
def check(s) :
    a = 0
    for i in s :
        if (i >='0' and i<='9') or i == '.' :
            a+=1
    if a == len(s) :
        return True
    else :
        return False    

def check_review(s) :
    a = 0
    for i in s :
        if (i >='0' and i<='9'):
            a+=1
    if a == len(s) :
        return True
    else :
        return False  

def check_string(s):
    for i in s :
        if (i>='a' and i<='z') or (i>='A' and i<='Z'):
            return False
    return True

def hide(choice):
    global e, hidden_text
    hidden_text= StringVar()
    if choice == "Paid":
        Label(screen18, text= 'Enter the price for the app:', fg='black').place(x=200, y=300) 
        e = Entry(screen18, textvariable = hidden_text, width=45)
        e.place(x=400, y=300)
    else:
        e = Entry(screen18, textvariable = hidden_text, width=45)
        e.place(x=400, y=300)

def validate() :
    if app_variable.get() != '' :
        if rating_variable.get() != '' and check(rating_variable.get()) :
            if review_variable.get() != '' and check_review(review_variable.get()) :
                if size_variable.get() != '' and check(size_variable.get()) :
                    if current_version_variable.get() != '' and check(current_version_variable.get()):
                        if android_version_variable.get() != '' and check(android_version_variable.get()) :
                            if category_variable.get() != '--Select Category--' and genre_variable.get() != '--Select Genre--' and install_variable.get() != '--Select No. of Installs--' and type_variable.get() != '--Select Type--'  and content_variable.get() != '--Select Content Rating--' and day_variable.get() != '--Select Day' and month_variable.get() != '--Select Month--' and year_variable.get() != '--Select Year--':
                                if type_variable.get() == 'Paid' and e.get() != '' and check(e.get()):
                                    app_cost = e.get()
                                    day_list = month_variable.get() + ' ' + day_variable.get() + ',' + year_variable.get()
                                    csv_data = []
                                    csv_data.append([app_variable.get(), category_variable.get(), rating_variable.get(), review_variable.get(), size_variable.get(), install_variable.get(),type_variable.get(), app_cost, content_variable.get(), genre_variable.get(), day_list, current_version_variable.get(), android_version_variable.get()])
                                    with open('dummy_data_1.csv', 'w') as csvFile:
                                        writer_row = writer(csvFile)
                                        writer_row.writerows(csv_data)
                                    csvFile.close()
                                    messagebox.showinfo("Success", "Data has been stored into the csv file!")
                                    screen18.destroy()
                                elif type_variable.get() == 'Free':
                                    app_cost = 0
                                    day_list = month_variable.get() + ' ' + day_variable.get() + ',' + year_variable.get()
                                    csv_data = []
                                    csv_data.append([app_variable.get(), category_variable.get(), rating_variable.get(), review_variable.get(), size_variable.get(), install_variable.get(),type_variable.get(), app_cost, content_variable.get(), genre_variable.get(), day_list, current_version_variable.get(), android_version_variable.get()])
                                    with open('dummy_data_1.csv', 'w') as csvFile:
                                        writer_row = writer(csvFile)
                                        writer_row.writerows(csv_data)
                                    csvFile.close()
                                    messagebox.showinfo("Success", "Data has been stored into the csv file!")
                                    screen18.destroy()
                                else :
                                    messagebox.showerror("Error", "Please enter a proper price for the app!", parent=screen18)
                            else :
                                messagebox.showerror("Error", "Please select an option from the drop list!", parent=screen18)
                        else :
                            messagebox.showerror("Error", "Please enter android version for the app!", parent=screen18)
                    else :
                        messagebox.showerror("Error", "Please enter current version for the app!", parent=screen18)
                else :
                    messagebox.showerror("Error", "Please enter any size for the app!", parent=screen18)
            else :
                messagebox.showerror("Error", "Please enter any number of reviews for the app!", parent=screen18)
        else :
            messagebox.showerror("Error", "Please enter any rating for the app!", parent=screen18)
    else :
        messagebox.showerror("Error", "Please fill in the name of the app!", parent=screen18)

def make_unique(dummy_list) :
    true_list = []
    for item in dummy_list :
        if item not in true_list  :
            true_list.append(item)
    return true_list 

def question_18() :
    global screen18, category_variable, genre_variable, install_variable, content_variable, type_variable, rating_variable, review_variable, size_variable, app_variable, current_version_variable, android_version_variable, month_variable, day_variable, year_variable
    screen18 = Tk()
    screen18.title('Question-18')
    adjustWindow(screen18)
    category_variable = StringVar(screen18)   
    genre_variable = StringVar(screen18)
    install_variable = StringVar(screen18)
    type_variable = StringVar(screen18)
    content_variable = StringVar(screen18)
    rating_variable = StringVar()
    review_variable = StringVar()
    size_variable = StringVar()
    app_variable = StringVar()
    current_version_variable = StringVar()
    android_version_variable = StringVar()
    month_variable = StringVar(screen18)
    day_variable = StringVar(screen18)
    year_variable = StringVar(screen18)
    Label(screen18, text= 'Fill up all the details of the app', fg='black').pack()
    Label(screen18, text= 'Enter name of the app : ', fg='black').place(x=230, y=40) 
    app_variable = Entry(screen18, width = 50)
    app_variable.place(x=400, y=40)
    dummy_category = data_naren['Category']
    categories = make_unique(dummy_category)
    #Label(screen18, text= 'Select Category', fg='black').place(x=50, y=320) 
    droplist_category = OptionMenu(screen18, category_variable, *categories) 
    category_variable.set('--Select Category--')
    droplist_category.config(width=20)  
    droplist_category.place(x=30, y=340)
    dummy_genre = data_naren['Genres']
    genres = make_unique(dummy_genre)
    #Label(screen18, text= 'Select Genre', fg='black').place(x=200, y=320) 
    droplist_genre = OptionMenu(screen18, genre_variable, *genres) 
    genre_variable.set('--Select Genre--') 
    droplist_genre.config(width=20) 
    droplist_genre.place(x=200, y=340)
    dummy_install = data_naren['Installs']
    installs = make_unique(dummy_install)
    #Label(screen18, text= 'Select No. of Installs', fg='black').place(x=350, y=320) 
    droplist_install = OptionMenu(screen18, install_variable, *installs) 
    install_variable.set('--Select No. of Installs--') 
    droplist_install.config(width=20) 
    droplist_install.place(x=370, y=340)
    dummy_type = data_naren['Type']
    types = make_unique(dummy_type)
    #Label(screen18, text= 'Select Type', fg='black').place(x=500, y=320) 
    droplist_type = OptionMenu(screen18, type_variable, *types, command = hide) 
    type_variable.set('--Select Type--') 
    droplist_type.config(width=20) 
    droplist_type.place(x=540, y=340)
    dummy_content = data_naren['Content Rating']
    contents = make_unique(dummy_content)
    droplist_content = OptionMenu(screen18, content_variable, *contents) 
    content_variable.set('--Select Content Rating--') 
    droplist_content.config(width=20) 
    droplist_content.place(x=710, y=340)
    Label(screen18, text= 'Enter rating for the app : ', fg='black').place(x=160, y=80) 
    rating_variable = Entry(screen18, width = 50)
    rating_variable.place(x=400, y=80)
    Label(screen18, text= 'Enter number of reviews for the app : ', fg='black').place(x=70, y=120) 
    review_variable = Entry(screen18, width = 50)
    review_variable.place(x=400, y=120)
    Label(screen18, text= 'Enter size of the app : ', fg='black').place(x=160, y=160) 
    size_variable = Entry(screen18, width = 50)
    size_variable.place(x=400, y=160)
    Label(screen18, text= 'Enter current version of the app : ', fg='black').place(x=210, y=200) 
    current_version_variable = Entry(screen18, width = 50)
    current_version_variable.place(x=400, y=200)
    Label(screen18, text= 'Enter android version of the app : ', fg='black').place(x=210, y=240) 
    android_version_variable = Entry(screen18, width = 50)
    android_version_variable.place(x=400, y=240)
    month_of_year = ['January','February','March','April','May','June','July','August','September','October','November','December']
    #Label(screen18, text= 'Enter month', fg='black').place(x=200, y=380) 
    droplist_month = OptionMenu(screen18, month_variable, *month_of_year) 
    month_variable.set('--Select Month--')
    droplist_month.config(width=20)  
    droplist_month.place(x=170, y=400)
    days_31 = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
    #Label(screen18, text= 'Enter day', fg='black').place(x=400, y=380) 
    droplist_day = OptionMenu(screen18, day_variable, *days_31) 
    day_variable.set('--Select Day--')
    droplist_day.config(width=20)  
    droplist_day.place(x=370, y=400)
    years_from_2015 = ['2015','2016','2017','2018','2019','2020','2021','2022','2023','2024','2025']
    #Label(screen18, text= 'Enter year', fg='black').place(x=600, y=380) 
    droplist_year = OptionMenu(screen18, year_variable, *years_from_2015) 
    year_variable.set('--Select Year--')
    droplist_year.config(width=20)  
    droplist_year.place(x=570, y=400)
    Button(screen18, text='Submit', width=20, font=("Open Sans", 13, 'bold'), bg='green', fg='white', command= validate).place(x=350, y=500) 
    button = Button(screen18, text="Quit", command=screen18.destroy)
    button.pack(side=BOTTOM)
    
def validate_2() :
    if application_variable.get() != '':
        if sentiment_option_variable.get() != '--Select Sentiment--': 
            if review_text.get("1.0",END) != '\n' :
                if check(sentiment_polarity_variable.get()) and check(sentiment_subjectivity_variable.get()):
                    csv_data = []
                    csv_data.append([application_variable.get(), sentiment_polarity_variable.get(), sentiment_subjectivity_variable.get(), sentiment_option_variable.get()])
                    with open('dummy_data_2.csv', 'w') as csvFile:
                        writer_row = writer(csvFile)
                        writer_row.writerows(csv_data)
                    csvFile.close()
                    messagebox.showinfo("Success", "Data has been stored into the csv file!")
                    screen18_2.destroy()
                else :
                    messagebox.showerror("Error", "Please enter a numeric value!", parent=screen18_2)
            else :
                messagebox.showerror("Error", "Please enter something in the reviews!", parent=screen18_2)
        else :
            messagebox.showerror("Error", "Please select an option from the drop list!", parent=screen18_2)
    else :
        messagebox.showerror("Error", "Please provide a name to the app!", parent=screen18_2)

def question_18_2() :
    global screen18_2, application_variable, sentiment_option_variable, sentiment_polarity_variable, sentiment_subjectivity_variable, review_text
    screen18_2 = Tk()
    screen18_2.title('Question-18_2')
    adjustWindow(screen18_2)
    application_variable = StringVar()
    sentiment_option_variable = StringVar(screen18_2)
    sentiment_polarity_variable = StringVar()
    sentiment_subjectivity_variable = StringVar()
    Label(screen18_2, text= 'Fill up all the details of the app', fg='black').pack()
    Label(screen18_2, text= 'Enter name of the app : ', fg='black').place(x=230, y=40) 
    application_variable = Entry(screen18_2, width=30)
    application_variable.place(x=400, y=40)
    sentiment_options = ['Positive', 'Negative', 'Neutral']
    Label(screen18_2, text= 'Select the sentiment for the app: ', fg='black').place(x=220, y=100) 
    droplist_category = OptionMenu(screen18_2, sentiment_option_variable, *sentiment_options) 
    sentiment_option_variable.set('--Select Sentiment--')
    droplist_category.config(width=20)  
    droplist_category.place(x=400, y=100)
    Label(screen18_2, text= 'Type the review for the app', fg='black').place(x=0, y=160) 
    review_text = Text(screen18_2, height=15, width=150)
    review_text.place(x=0, y=180)
    review_text.configure(state='normal')
    Label(screen18_2, text= 'Select the sentiment polarity for the app(use decimal point): ', fg='black').place(x=90, y=450) 
    sentiment_polarity_variable = Entry(screen18_2, width=20)
    sentiment_polarity_variable.place(x=450, y=450)
    Label(screen18_2, text= 'Select the sentiment subjectivity for the app(use decimal point): ', fg='black').place(x=90, y=490) 
    sentiment_subjectivity_variable = Entry(screen18_2, width=20)
    sentiment_subjectivity_variable.place(x=450, y=490)
    Button(screen18_2, text='Submit', width=20, font=("Open Sans", 13, 'bold'), bg='green', fg='white', command= validate_2).place(x=350, y=550)
    button = Button(screen18_2, text="Quit", command=screen18_2.destroy)
    button.pack(side=BOTTOM) 
    
def question_18_first_page() :
    global screen18_first
    screen18_first = Tk()
    screen18_first.title('Question-18-First')
    adjustWindow(screen18_first)
    Label(screen18_first, text= 'Choose any dataset for filling the details of the app', fg='black').pack()
    Button(screen18_first, text='Dataset-1', width=50, height=10, font=("Open Sans", 13, 'bold'), bg='green', fg='white', command= question_18).place(x=200, y=100) 
    Button(screen18_first, text='Dataset-2', width=50, height=10, font=("Open Sans", 13, 'bold'), bg='green', fg='white', command= question_18_2).place(x=200, y=400) 
    button = Button(screen18_first, text="Quit", command=screen18_first.destroy)
    button.pack(side=BOTTOM)

def question_4() :
    global screen4
    screen4 = Tk()
    screen4.title('Question-4')
    adjustWindow(screen4)
    category = data_naren['Category']
    ratings = data_naren['Rating']
    category_list = [] 
    ratings_list = []
    true_ratings = []
    cat_list = []
    for rate in ratings :
        true_ratings.append(rate)
    for cat in category :
        if cat not in category_list:
            category_list.append(cat)
        cat_list.append(cat)
    for cate in category_list :
        sum_of_ratings = 0
        den = 0
        for i in range(len(cat_list)) :
            if cate == cat_list[i] :
                den += 1
                sum_of_ratings += true_ratings[i]
        ratings_list.append(sum_of_ratings/den)
    max_rating = max(ratings_list)
    res_category = category_list[ratings_list.index(max_rating)]
    res_rating = max_rating
    #set(style="darkgrid")
    f, ax = subplots(figsize=(9, 7))
    Label(screen4, text='Category to get highest maximum average rating: '+category_list[ratings_list.index(max_rating)], font=("Open Sans", 15, 'bold'), fg='black').pack() 
    title('Category with highest maximum average ratings', size=20)
    rects = bar(res_category, res_rating, color='green')
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.01*height,'%.2f' % float(height),ha='center', va='bottom')
    xlabel('Category')
    ylabel('Rating')
    show()
    canvas = FigureCanvasTkAgg(f, screen4) 
    canvas.draw()
    canvas.get_tk_widget().pack(side = TOP, fill = BOTH, expand = True)    
    button = Button(screen4, text="Quit", command=screen4.destroy)
    button.pack(side=BOTTOM)

def function6():
    global screen9 
    screen9 = Toplevel(screen) 
    screen9.title("FUNCTION 5")
    adjustWindow(screen9)
      
    data_naren1=data_naren[(data_naren['Year']>=2015)&(data_naren['Year']<=2018)]
    plt.subplots(figsize=(6,6))
    plt.title("DOWNLOAD TREND CATEGORY WISE")
    sns.countplot(x="Category",hue='Year',data=data_naren1)
    plt.xticks(fontsize=6,rotation=78)
    plt.savefig('C:\\Users\\Admin\\Desktop\\internship gui\\function6.jpg',dpi=100)
  
    img = ImageTk.PhotoImage(Image.open('.function6.png'))
    panel =Label(screen9, image = img)
    panel.pack(side="bottom", fill="both",expand="yes")
    
    screen9.mainloop()
    
def function7():
    global screen10 
    screen10 = Toplevel(screen) 
    screen10.title("FUNCTION 7")
    adjustWindow(screen10)
      
    plt.subplots(figsize=(6,6))
    plt.title("THE PERCENTAGE OF DOWNLOADS AS ANDROID VERSION")
    sns.countplot(data_naren['Android Ver'],label='percentage')
    plt.xticks(fontsize=6,rotation=78)
    plt.savefig('C:\\Users\\Admin\\Desktop\\internship gui\\function7.jpg',dpi=100)

    img = ImageTk.PhotoImage(Image.open('function7.jpg'))
    panel =Label(screen10, image = img)
    panel.pack(side="bottom", fill="both",expand="yes")
    
    screen10.mainloop()
 

def function9():
    global screen12 
    screen12 = Toplevel(screen) 
    screen12.title("FUNCTION 9")
    adjustWindow(screen12)
    
    l1=data_naren.loc[(data_naren['Installs']=='100000'),['Installs','App']].count()
    l=data_naren.loc[(data_naren['Rating']==4.1)&(data_naren['Installs']=='100000'),['Installs','App']].count()
    Label(screen12, text="Apps with downloads 100,000+", bg='yellow', fg='black').pack()
    Label(screen12, text=l1, bg='yellow', fg='black').pack()
    Label(screen12, text="Apps with rating 4.1 & downloads 100,000+", bg='yellow', fg='black').pack()
    Label(screen12, text=l, bg='yellow', fg='black').pack()
    
    screen12.mainloop()

def function10():
    global screen13 
    screen13 = Toplevel(screen) 
    screen13.title("FUNCTION 9")
    adjustWindow(screen13)
    
    data_naren['Month'] = pd.DatetimeIndex(data_naren['Last Updated']).month
    
    contentrating_list=data_harsh['Content Rating'].tolist()
    
    l=contentrating_list.count('Teen')
    l1=contentrating_list.count('Mature 17+')
    Label(screen13, text="Total number of teen rating apps", bg='yellow', fg='black').pack()
    Label(screen13, text=l, bg='yellow', fg='black').pack()
    Label(screen13, text="Total number of Mature 17+ rating apps ", bg='yellow', fg='black').pack()
    Label(screen13, text=l1, bg='yellow', fg='black').pack()          
    
    installs = data_naren['Installs']
    category = data_naren['Category']
    content_rating =data_naren['Content Rating']
    teen_install = 0
    mature_install = 0
    months = []
    cat_list = []
    install_list = []
    dum = []
    content_rating_list = []
    max_install_list = []
    category_list = []
    for content in content_rating :
        content_rating_list.append(content)
    for cat in category :
        if cat not in category_list :
            category_list.append(cat)
            cat_list.append(cat)
    for date in dates:
        month = date[0:-8].split()
        months.append(month)
    for install in installs :
        if install == 'Free' :
            install_list.append(0)
        else :
            install_list.append(int(install))
    for i in range(len(content_rating_list)) :
            if content_rating_list[i] == 'Teen' :        
                teen_install += install_list[i]
            if content_rating_list[i] == 'Mature 17+' :
                mature_install += install_list[i]
    e1=(teen_install/mature_install)
    
    Label(screen13, text="Ratio of teen vs mature 17 is", bg='yellow', fg='black').pack()
    Label(screen13, text=e1, bg='yellow', fg='black').pack()
    
    screen13.mainloop()
    
#extra feature year and category
def functionextra1():
    global screen69,catname2,yearnum
    app_name=StringVar()
    screen69 = Toplevel(screen) 
    screen69.title("FUNCTION 14")
    #adjustWindow(screen24) 
    screen69.geometry("490x310")
    screen.resizable(False,False)
    data_naren['Year'] = pd.DatetimeIndex(data_naren['Last Updated']).year
    photo14 = PhotoImage(file="dark.png") # opening right side image - Note: If image is in same folder then no need to mention the full path 
    label14 = Label(screen69, image=photo14, text="") # attaching image to the label 
    label14.place(x=-12, y=-12) 
    label14.image = photo14 # it is necessary in Tkinter to keep a instance of image to display image in label 
    data_naren['quarter_year'] = pd.to_datetime(data_naren['Last Updated']).dt.to_period('Q')
    catname2= StringVar(screen69)
    catname2.set("drop down menu button")
    
    yearnum= StringVar(screen69)
    yearnum.set("drop down menu button")
    
    def grab_and_assign5(event):
        global chosen_option
        chosen_option1 = catname2.get() 
        label_chosen_variable= Label(screen69, text=chosen_option1)
        label_chosen_variable.pack()
    
    def grab_and_assign6(event):
        global chosen_option
        chosen_option2 = yearnum.get() 
        label_chosen_variable= Label(screen69, text=chosen_option2)
        label_chosen_variable.pack()
        
    drop_menu = OptionMenu(screen69,catname2,'ART_AND_DESIGN','AUTO_AND_VEHICLES','BEAUTY','BOOKS_AND_REFERENCE','BUSINESS','COMICS','COMMUNICATION','DATING','EDUCATION','ENTERTAINMENT','EVENTS','FINANCE','FOOD_AND_DRINK','HEALTH_AND_FITNESS','HOUSE_AND_HOME','LIBRARIES_AND_DEMO','LIFESTYLE','GAME','FAMILY','MEDICAL','SOCIAL','SHOPPING','PHOTOGRAPHY','SPORTS','TRAVEL_AND_LOCAL','TOOLS','PERSONALIZATION','PRODUCTIVITY','PARENTING','WEATHER','VIDEO_PLAYERS','NEWS_AND_MAGAZINES','MAPS_AND_NAVIGATION',command=grab_and_assign5)
    drop_menu.pack()#drop_menu.grid(row=0, column=0)
    
    drop_menu = OptionMenu(screen69,yearnum,'2011','2012','2013','2014','2015','2016','2017','2018Q1',command=grab_and_assign6)
    drop_menu.pack()#drop_menu.grid(row=0, column=0)
    
           
    Button(screen69, text="Proceed", height="2", width="30",  bg='brown', font=("Open Sans", 10, 'bold'), fg='white', command=functionextrasub).place(x=120,y=220)
    
    screen69.mainloop()

def functionextrasub():
    global screen70,catname2,yearnum
    screen70 = Toplevel(screen) 
    screen70.title("FUNCTION 14")
    adjustWindow(screen70)
    #screen25.geometry("800x800")
    chosen_option1 = catname2.get()
    chosen_option2 = yearnum.get()
    data_naren['Year'] = pd.DatetimeIndex(data_naren['Last Updated']).year
    data_naren['quarter_year'] = pd.to_datetime(data_naren['Last Updated']).dt.to_period('Q')
    t1=data_naren.loc[(data_naren['Category']==chosen_option1)&(data_naren['quarter_year']==chosen_option2),['Installs','App']].count()
    Label(screen70, text=t1, bg='yellow', fg='black').pack()
    plt.subplots(figsize=(6,6))
    plt.title("THE PERCENTAGE OF DOWNLOADS CATEGORY WISE")
    sns.countplot(data_naren['Category']==chosen_option1,hue=data_naren['quarter_year']==chosen_option2)
    plt.xticks(fontsize=6,rotation=78)
    plt.savefig('C:\\Users\\Admin\\Desktop\\internship gui\\function5.jpg',dpi=100)
    
    img = ImageTk.PhotoImage(Image.open('function5.jpg'))
    panel =Label(screen70, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")
    
    screen70.mainloop()
    
def question_16() :
    global screen16
    screen16 = Tk()
    screen16.title('Function-16')
    adjustWindow(screen16)
    dates = data_naren['Last Updated']
    installs = data_naren['Installs']
    default_months = ['January','February','March','April','May','June','July','August','September','October','November','December']
    imp_months = []
    years = []
    months = []
    install_list = []
    true_year_list = []
    dum = []
    loop_months = []
    month_installs = []
    month_installs_list = []
    dis_res = []
    dic = {}
    for install in installs :
        if install == 'Free' :
            install_list.append(0)
        else :
            install_list.append(int(install))
    for date in dates :
        years.append(date[-4:])
        month = date[0:-8].split()
        months.append(month)
    for year in years :
        if year not in true_year_list :
            true_year_list.append(year)
    for year in true_year_list :
        month_installs = []
        for month in default_months :
            dum = []
            sum_of_installs = 0
            dum.append(month)
            for i in range(len(months)) :
                if dum == months[i] and years[i] == year:
                    sum_of_installs += install_list[i]
            month_installs.append(sum_of_installs)
        myNumber = sum(month_installs)/12
        imp_months.append(default_months[month_installs.index(min(month_installs, key=lambda x:abs(x-myNumber)))])
        month_installs_list.append(month_installs)
    for m in imp_months :
        if m not in loop_months :
            loop_months.append(m)
    for month1 in loop_months :
        count = 0
        for month2 in imp_months :
            if month1 == month2 :
                count += 1
        dic.update({month1:count})
    max_val = max(dic.values())
    for key, value in dic.items() :
        if value == max_val :
            dis_res.append(key)
    default_months_list = ['Ja','Fe','Ma','Ap','My','Jn','Jy','Au','Sp','Oc','No','De']
    #set(style="darkgrid")
    f, ax = subplots(figsize=(9, 7))
    Label(screen16, text= 'Months that are the best indicator for average downloads over all years : '+dis_res[0], font=("Open Sans", 15, 'bold'), fg='black').pack() 
    for k in range(1, len(month_installs_list)+1) :     
        subplot(4, 3, k)
        title(true_year_list[k-1]+'('+imp_months[k-1]+')', size=20)
        rects = bar(default_months_list, month_installs_list[k-1])
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2., 1.01*height,'%.1f' % float(height),ha='center', va='bottom')
        xlabel('Months')
        ylabel('Installs')
        tight_layout()
    show()
    canvas = FigureCanvasTkAgg(f, screen16) 
    canvas.draw()
    canvas.get_tk_widget().pack(side = TOP, fill = BOTH, expand = True)    
    button = Button(screen16, text="Quit", command=screen16.destroy)
    button.pack(side=BOTTOM)
    
def function15():
    global screen18 
    screen18 = Toplevel(screen) 
    screen18.title("FUNCTION 15")
    adjustWindow(screen18)

    
    sentiment_list=data_priya['Sentiment'].head(201).tolist()

    a1=sentiment_list.count('Positive')
    a2=sentiment_list.count('Negative')
    a3=sentiment_list.count('Neutral')
    a4=sentiment_list.count('nan')
    
    Label(screen18, text="Total number of Positive Sentiments", bg='yellow', fg='black').pack()
    Label(screen18, text=a1, bg='yellow', fg='black').pack()
    Label(screen18, text="Total number of Negative Sentiments", bg='yellow', fg='black').pack()
    Label(screen18, text=a2, bg='yellow', fg='black').pack()
    Label(screen18, text="Total number of Neutral Sentiments", bg='yellow', fg='black').pack()
    Label(screen18, text=a3, bg='yellow', fg='black').pack()
    Label(screen18, text="Total number of null sentimental data", bg='yellow', fg='black').pack()
    Label(screen18, text=a4, bg='yellow', fg='black').pack()
    
    y=int(str(len(data_priya.head(201))))    
    
    b1=(sentiment_list.count('Positive')/y)*100
    b2=(sentiment_list.count('Negative')/y)*100
    b3=(sentiment_list.count('Neutral')/y)*100
    
    
    Label(screen18, text="Percentage of Positive Sentiments", bg='yellow', fg='black').pack()
    Label(screen18, text=b1, bg='yellow', fg='black').pack()
    Label(screen18, text="Percentage of Negative Sentiments", bg='yellow', fg='black').pack()
    Label(screen18, text=b2, bg='yellow', fg='black').pack()
    Label(screen18, text="Percentage of Neutral Sentiments", bg='yellow', fg='black').pack()
    Label(screen18, text=b3, bg='yellow', fg='black').pack()

    
    screen18.mainloop()
    
def question_12():
    global screen12
    screen12 = Tk()
    screen12.title('Question-12')
    adjustWindow(screen12)
    dummy_app_data = data_priya['App']
    sentiments = data_priya['Sentiment']
    app_data = []
    pos_list = []
    neg_list = []
    needed_apps = []
    sentiment_list = []
    apps_list = []       
    send_required_parameters = []
    for app in dummy_app_data :
        if app not in app_data :
            app_data.append(app)
        apps_list.append(app)
    for senti in sentiments :
        sentiment_list.append(senti)
    for app in app_data :
        pos = 0
        neg = 0
        for i in range(len(sentiment_list)) :
            if app == apps_list[i] :
                if sentiment_list[i] == 'Positive' :
                    pos += 1
                if sentiment_list[i] == 'Negative' :
                    neg += 1
        if pos != 0 and neg != 0 :  
            needed_apps.append(app)
            pos_list.append(pos)
            neg_list.append(neg)
    max_pos = max(pos_list)
    max_neg = max(neg_list)
    sentiments_list = ['Positive', 'Negative']
    a = [pos_list[pos_list.index(max_pos)], neg_list[pos_list.index(max_pos)]]
    b = [pos_list[neg_list.index(max_neg)], neg_list[neg_list.index(max_neg)]]
    for i in range(len(pos_list)) :
        if pos_list[i] == neg_list[i] :
            send_required_parameters.append([needed_apps[i], pos_list[i]])
    button1 = Button(screen12, text="App with the most negative sentiments", command= lambda: display_negative_sentiment_app(sentiments_list, b, colors, needed_apps, neg_list, max_neg))
    button1.pack()
    button = Button(screen12, text="Click to know the apps with same number of positive and negative sentiments", command= lambda: display_same_sentiments(send_required_parameters))
    button.pack()
    #set(style="darkgrid")
    f, ax = subplots(figsize=(9, 7))
    colors = ['green', 'red']
    rects = bar(sentiments_list,a, color=colors)
    title(needed_apps[pos_list.index(max_pos)], size=20)
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.01*height,
                '%.1f' % float(height),
        ha='center', va='bottom')
    xlabel('Sentiments')
    ylabel('Count')
    show()
    canvas = FigureCanvasTkAgg(f, screen12) 
    canvas.draw()
    canvas.get_tk_widget().pack(side = TOP, fill = BOTH, expand = True)    
    button = Button(screen12, text="Quit", command=screen12.destroy)
    button.pack(side=BOTTOM)
    
def display_negative_sentiment_app(sentiments_list, b, colors, needed_apps, neg_list, max_neg) :
    global screen12_2, same_count_list
    screen12_2 = Tk()
    screen12_2.title('Question-12.2')
    adjustWindow(screen12_2)
    #set(style="darkgrid")
    f, ax = subplots(figsize=(9, 7))
    rects = bar(sentiments_list,b, color=colors)
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.01*height,'%.1f' % float(height),ha='center', va='bottom')
    xlabel('Sentiments')
    ylabel('Count')
    title(needed_apps[neg_list.index(max_neg)], size=20)
    show()
    canvas = FigureCanvasTkAgg(f, screen12_2) 
    canvas.draw()
    canvas.get_tk_widget().pack(side = TOP, fill = BOTH, expand = True)    
    button = Button(screen12_2, text="Quit", command=screen12_2.destroy)
    button.pack(side=BOTTOM)

def display_same_sentiments(send_required_parameters) :
    global screen12_1, same_count_list
    screen12_1 = Tk()
    screen12_1.title('Question-12.1')
    adjustWindow(screen12_1)
    display_app_list = []
    display_count_list = []
    for parameter in send_required_parameters :
        display_app_list.append(parameter[0])
        display_count_list.append(parameter[1])
    Label(screen12_1, text= 'Apps with count', fg='black').pack() 
    same_count_list = Text(screen12_1, height=20, width=100)
    for i in range(len(display_app_list)) :
        same_count_list.insert(END, display_app_list[i]+'   --->   '+str(display_count_list[i])+'\n')
    same_count_list.pack()
    same_count_list.configure(state='disabled')
    button = Button(screen12_1, text="Quit", command=screen12_1.destroy)
    button.pack(side=BOTTOM)
    
def question_1() :
    global screen1
    screen1 = Tk()
    screen1.title('Question-1')
    adjustWindow1(screen1)
    category = data_naren['Category']
    category_list=  []
    install_list = []
    sum_install_list = []
    cat_list = []
    display_sum_list = []
    installs = data_naren['Installs']
    for install in installs :
        if install == 'Free':
            install_list.append(0)
        else :
            install_list.append(int(install))  
    for cat in category :
        if cat not in category_list :
            category_list.append(cat)
        cat_list.append(cat)
    for cat in category_list :
        dummy_sum = 0
        for i in range(len(cat_list)) :
            if cat == cat_list[i] :
                dummy_sum += install_list[i]
        sum_install_list.append(dummy_sum)
    for ele in sum_install_list :
        display_sum_list.append((ele * 100) / sum(install_list))
    f, ax = subplots(figsize=(11, 9))
    #set(style="darkgrid")
    colors = ['yellow','black','maroon','purple','tomato','coral','salmon','khaki','olive','lime','cyan','turquoise','navy','indigo','thistle','plum','violet','orchid','pink','beige','wheat','peru','chocolate','tan','linen','lavender','ivory','honeydew','azure','snow','gainsboro','silver','grey','moccasin']
    title('Percentage Downloads of each category', size=20)
    rects = bar(category_list, display_sum_list, color=colors)
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.01*height,'%.1f' % float(height) + '%',ha='center', va='bottom')
    xticks(rotation=90)
    xlabel('Category')
    ylabel('Installs')
    show()
    canvas = FigureCanvasTkAgg(f, screen1) 
    canvas.draw()
    canvas.get_tk_widget().pack(side = TOP, fill = BOTH, expand = True)    
    button = Button(screen1, text="Quit", command=screen1.destroy)
    button.pack(side=BOTTOM)    

def question_14() :
    global screen14, category_variable, droplist_app, droplist_category
    screen14 = Tk()
    screen14.title('Question-14')
    adjustWindow(screen14) 
    category_variable = StringVar(screen14)
    apps_list_1 = data_naren['App']
    apps_1 = []
    required_apps_from_1 = []
    category_list_1 = data_naren['Category']
    categories = []
    required_category_from_1 = []
    required_unique_categories = []
    apps_list_2 = data_priya['App']
    apps_2 = []
    apps_unique_2 = []
    required_unique_apps = []      
    for cat in category_list_1 :
        categories.append(cat)
    for app in apps_list_2 :
        if app not in apps_unique_2 :
            apps_unique_2.append(app)
        apps_2.append(app)
    for app in apps_list_1 :
        apps_1.append(app)
    for app in apps_unique_2 :
        for i in range(len(apps_1)) :
            if app == apps_1[i] :
                required_category_from_1.append(categories[i])
                required_apps_from_1.append(app)
    for each_category in required_category_from_1 :
        if each_category not in required_unique_categories :
            required_unique_categories.append(each_category)
    for element in required_unique_categories :
        dummy_apps = []
        for i in range(len(required_category_from_1)) :
            if element == required_category_from_1[i] and required_apps_from_1[i] not in dummy_apps:
                dummy_apps.append(required_apps_from_1[i])
        required_unique_apps.append(dummy_apps)   
    Label(screen14, text= 'Category', fg='black').pack() 
    category_variable.set('--Select Category--') 
    droplist_category = OptionMenu(screen14, category_variable, *required_unique_categories)
    droplist_category.config(anchor='center', width=35) 
    droplist_category.pack()
    button1 = Button(screen14, text="Tap", command= lambda: display_apps(required_unique_categories, required_unique_apps))
    button1.pack()
    button = Button(screen14, text="Quit", command=screen14.destroy)
    button.pack(side=BOTTOM)

def display_reviews(app_list, apps, sentiments, reviews) :
    global caught_app_variable
    caught_app_variable = StringVar()
    caught_app_variable = app_variable.get()      
    if caught_app_variable != "--Select App--" :
        positive_text.delete('1.0', END)
        negative_text.delete('1.0', END)
        neutral_text.delete('1.0', END)
        scroll=Scrollbar(positive_text)
        positive_text.configure(state='normal')
        negative_text.configure(state='normal')
        neutral_text.configure(state='normal')
        positive_list = []
        negative_list = []
        neutral_list = [] 
        positive = 0
        negative = 0
        neutral = 0
        for app in app_list :
            for i in range(len(apps)) :
                if caught_app_variable == apps[i] and sentiments[i] == 'Positive' and reviews[i] not in positive_list:
                    positive += 1
                    positive_text.insert(END, str(positive)+'--> '+reviews[i]+'\n\n')
                    positive_list.append(reviews[i])
                if caught_app_variable == apps[i] and sentiments[i] == 'Negative' and reviews[i] not in negative_list:
                    negative += 1
                    negative_text.insert(END, str(negative)+'--> '+reviews[i]+'\n\n')
                    negative_list.append(reviews[i])
                if caught_app_variable == apps[i] and sentiments[i] == 'Neutral' and reviews[i] not in neutral_list:
                    neutral += 1
                    neutral_text.insert(END, str(neutral)+'--> '+reviews[i]+'\n\n')
                    neutral_list.append(reviews[i])
    else :
        messagebox.showerror("Error", "Please select any app from the drop list!", parent=screen14_1)
    positive_text.configure(yscrollcommand=scroll.set)
    negative_text.configure(yscrollcommand=scroll.set)
    neutral_text.configure(yscrollcommand=scroll.set)
    
def display_apps(required_unique_categories, required_unique_apps) :
    global screen14_1, app_variable, caught_category_variable, positive_text, negative_text, neutral_text, apps_to_display
    caught_category_variable = StringVar()
    caught_category_variable = category_variable.get()
    if caught_category_variable == "--Select Category--" :
        messagebox.showerror("Error", "Please select any category from the drop list!", parent=screen14)
    else :
        screen14_1=  Tk()
        screen14_1.title('Question-14.1')
        adjustWindow(screen14_1) 
        app_variable = StringVar(screen14_1)
        apps_2 = []
        apps_list_2 = data_priya['App']
        sentiments_list = data_priya['Sentiment']
        sentiments = []
        reviews_list = data_priya['Translated_Review']
        reviews= []
        for review in reviews_list :
            reviews.append(review)
        for sentiment in sentiments_list :
            sentiments.append(sentiment)
        for app in apps_list_2 :
            apps_2.append(app)
        for cat in range(len(required_unique_categories)) :
            if required_unique_categories[cat] == caught_category_variable :
                apps_to_display = required_unique_apps[cat]
                break
        Label(screen14_1, text= 'App', fg='black').pack()
        droplist = OptionMenu(screen14_1, app_variable, *apps_to_display) 
        droplist.config(anchor='center', width=35) 
        app_variable.set('--Select App--') 
        droplist.pack()
        button2 = Button(screen14_1, text="Watch", command= lambda: display_reviews(apps_to_display, apps_2, sentiments, reviews))
        button2.pack()
        Label(screen14_1, text= 'Positive', fg='black').pack() 
        positive_text = Text(screen14_1, height=9, width=100)
        positive_text.pack()
        positive_text.configure(state='disabled')
        Label(screen14_1, text= 'Negative', fg='black').pack() 
        negative_text = Text(screen14_1, height=9, width=100)
        negative_text.pack()
        negative_text.configure(state='disabled')
        Label(screen14_1, text= 'Neutral', fg='black').pack() 
        neutral_text = Text(screen14_1, height=9, width=100)
        neutral_text.pack()
        neutral_text.configure(state='disabled')
        button = Button(screen14_1, text="Quit", command=screen14_1.destroy)
        button.pack(side=BOTTOM)

def question_2() :
    global screen2
    screen2 = Tk()
    screen2.title('Question-2')
    adjustWindow(screen2)
    app_list = []
    install_list = []
    first_list_installs = []
    first_list_apps = []
    second_list_installs = []
    second_list_apps = []
    third_list_installs = []
    third_list_apps = []
    fourth_list_installs = []
    fourth_list_apps = []
    fifth_list_installs = []
    fifth_list_apps = []
    installs = data_naren['Installs']
    apps = data_naren['App']
    for app in apps :
        app_list.append(app)
    for install in installs :
        if install == 'Free' :
            install_list.append(0)
        else :
            install_list.append(int(install)) 
    for i in range(len(install_list)) :
        if install_list[i] >= 10000 and install_list[i] < 50000 :
            first_list_installs.append(install_list[i])
            first_list_apps.append(app_list[i])
        if install_list[i] >= 50000 and install_list[i] < 150000 :
            second_list_installs.append(install_list[i])
            second_list_apps.append(app_list[i])
        if install_list[i] >= 150000 and install_list[i] < 500000 :
            third_list_installs.append(install_list[i])
            third_list_apps.append(app_list[i])
        if install_list[i] >= 500000 and install_list[i] < 5000000 :
            fourth_list_installs.append(install_list[i])
            fourth_list_apps.append(app_list[i])
        if install_list[i] >= 5000000 :
            fifth_list_installs.append(install_list[i])
            fifth_list_apps.append(app_list[i])         
    #set(style="darkgrid")
    f, ax = subplots(figsize=(9, 7))
    ranges = ['10,000-50,000', '50,000-150000', '150000-500000', '500000-5000000', 'More than 5000000']
    apps_list = [len(first_list_apps), len(second_list_installs), len(third_list_installs), len(fourth_list_installs), len(fifth_list_installs)]
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'red']
    title('Total number of apps for ranges', size=20)
    rects = bar(ranges, apps_list, color=colors)
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.01*height,'%.1f' % float(height),ha='center', va='bottom')
    xlabel('Ranges')
    ylabel('Number of Apps')
    xticks(rotation=90)
    show()
    canvas = FigureCanvasTkAgg(f, screen2) 
    canvas.draw()
    canvas.get_tk_widget().pack(side = TOP, fill = BOTH, expand = True)    
    button = Button(screen2, text="Quit", command=screen2.destroy)
    button.pack(side=BOTTOM)
    
def question_15() :
    global screen15
    screen15 = Tk()
    screen15.title('Question-15')
    adjustWindow(screen15)
    data = data_priya[data_priya['App'] == '10 Best Foods for You']
    x = data_priya['Sentiment']
    sentiments = []
    x_list = []
    sentiments_count = []
    d = {}
    for senti in x :
        if senti not in sentiments :
            sentiments.append(senti)
        x_list.append(senti)
    for i in sentiments :
        c = 0
        for j in x_list :
            if i == j :
                c += 1
        sentiments_count.append(c)
        d.update({i:c})
    var = max(d.values())
    for key, value in d.items(): 
        if key == 'Negative' :
            if value >= round(var/2) :
                Label(screen15, text="10 Best Foods for You - This app should not be launched!", font=("Open Sans", 15, 'bold'), fg='black').pack()
            else :
                Label(screen15, text="10 Best Foods for You - This app should be launched!", font=("Open Sans", 15, 'bold'), fg='black').pack() 
    #set(style="darkgrid")
    f, ax = subplots(figsize=(9, 7))
    colors = ['red','blue','green']
    title('Sentiments analysis for app :"10 Best Foods for You" ', size=20)
    rects = bar(sentiments, sentiments_count, color=colors)
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.01*height,
                '%.1f' % float(height),
        ha='center', va='bottom')
    xlabel('Sentiments')
    ylabel('Count')
    show()
    canvas = FigureCanvasTkAgg(f, screen15) 
    canvas.draw()
    canvas.get_tk_widget().pack(side = TOP, fill = BOTH, expand = True)    
    button = Button(screen15, text="Quit", command=screen15.destroy)
    button.pack(side=BOTTOM)
    
def display_relation(left_bar, right_bar) :
    global screen13_1
    screen13_1 = Tk()
    screen13_1.title('Question-13.1')
    adjustWindow(screen13_1)
    left_bar = array(left_bar)
    left_bar = left_bar.reshape(-1,1)
    right_bar = array(right_bar)
    right_bar = right_bar.reshape(-1,1)
    reg = LinearRegression()
    reg.fit(left_bar, right_bar)
    relation_predictions = reg.predict(left_bar)
    X2 = add_constant(left_bar)
    est = OLS(right_bar,X2)
    est2 = est.fit()
    f, ax = subplots(figsize=(9, 7))
    Label(screen13_1, text= 'Linear Model : Y = {:.5}X + {:.5}'.format(reg.coef_[0][0],reg.intercept_[0]), fg='black').pack() 
    Label(screen13_1, text= 'Accuracy : {}'.format(est2.rsquared), fg='black').pack() 
    scatter(left_bar, right_bar, c='black')
    plot(left_bar,relation_predictions,c='red',linewidth=2)
    xlabel('Sentiment Polarity')
    ylabel('Sentiment Subjectivity')
    show()
    canvas = FigureCanvasTkAgg(f, screen13_1) 
    canvas.draw()
    canvas.get_tk_widget().pack(side = TOP, fill = BOTH, expand = True) 
    button = Button(screen13_1, text="Quit", command=screen13_1.destroy)
    button.pack(side=BOTTOM)
    
def question_13() :
    global screen13
    screen13 = Tk()
    screen13.title('Question-13')
    adjustWindow(screen13)
    sentiment_polarity = []
    sentiment_subjectivity = []
    unique_apps_list = []
    apps = []
    sum_sp = 0
    sum_ss = 0
    sentiment_polarity_list = data_priya['Sentiment_Polarity']
    sentiment_subjectivity_list = data_priya['Sentiment_Subjectivity']
    apps_list = data_priya['App']
    for app in apps_list :
        if app not in unique_apps_list :
            unique_apps_list.append(app)
        apps.append(app)
    for sp in sentiment_polarity_list :
        sentiment_polarity.append(sp)
    for ss in sentiment_subjectivity_list :
        sentiment_subjectivity.append(ss)
    for i in range(len(apps)) :
        sum_sp += sentiment_polarity[i]
        sum_ss += sentiment_subjectivity[i]
    ss_sp_list = ['Sentiment-Subjectivity', 'Sentiment-Polarity']
    ss_sp_sum = [sum_ss, sum_sp]
    set(style="darkgrid")
    f, ax = subplots(figsize=(9, 7))
    Label(screen13, text= 'For value = 1 of sentiment polarity, approximate value of sentiment subjectivity: {}'.format(round(sum_ss / sum_sp)), fg='black').pack() 
    rects = bar(ss_sp_list, ss_sp_sum, color=['red', 'blue'])
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.01*height,
                '%.1f' % float(height),
        ha='center', va='bottom')
    xlabel('Sentiments')
    ylabel('Values')
    show()
    canvas = FigureCanvasTkAgg(f, screen13) 
    canvas.draw()
    canvas.get_tk_widget().pack(side = TOP, fill = BOTH, expand = True) 
    button = Button(screen13, text="Quit", command=screen13.destroy)
    button.pack(side=BOTTOM)
    
def display_trend(categories) :
    global screen5_1, category_variable_catch
    category_variable_catch = StringVar()
    category_variable_catch = category_variable_q5.get()
    if category_variable_catch == "--Select Category--" :
        messagebox.showerror("Error", "Please select any category from the drop list!", parent=screen5)
    else :
        screen5_1 = Tk()
        screen5_1.title('Question-5_1')
        adjustWindow(screen5_1)
        dates = data_naren['Last Updated']
        years = []
        install_list = []
        display_install_trend = []
        installs = data_naren['Installs']
        for install in installs :
            if install == 'Free' :
                install_list.append(0)
            else :
                install_list.append(int(install))
        for date in dates :
            years.append(date[-4:])
        years_list = ['2010','2011','2012','2013','2014','2015','2016','2017','2018']
        for year in years_list :
            year_install = 0
            for i in range(len(categories)) :
                if categories[i] == category_variable_catch and year == years[i]:
                    year_install += install_list[i]
            display_install_trend.append(year_install)
        #set(style="darkgrid")
        f, ax = subplots(figsize=(9, 7))
        colors = ['khaki','blue','green','yellow','orange','gold','violet','maroon','red']
        title('Download trend for '+category_variable_catch, size=20)
        rects = bar(years_list, display_install_trend, color = colors)
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width()/2., 1.01*height,'%.1f' % float(height),ha='center', va='bottom')
        xlabel('Years')
        ylabel('Installs')
        show()
        canvas = FigureCanvasTkAgg(f, screen5_1) 
        canvas.draw()
        canvas.get_tk_widget().pack(side = TOP, fill = BOTH, expand = True)    
        button = Button(screen5_1, text="Quit", command=screen5_1.destroy)
        button.pack(side=BOTTOM)
    
def question_5() :
    global screen5, category_variable_q5
    screen5 = Tk()
    screen5.title('Question-5')
    adjustWindow(screen5)
    category_list = data_naren['Category']
    categories = []
    unique_categories = []
    for cat in category_list :
        if cat not in unique_categories :
            unique_categories.append(cat)
        categories.append(cat)
    category_variable_q5 = StringVar(screen5)
    Label(screen5, text= 'Category', fg='black').pack() 
    category_variable_q5.set('--Select Category--') 
    droplist_category_q5 = OptionMenu(screen5, category_variable_q5, *unique_categories)
    droplist_category_q5.config(anchor='center', width=35) 
    droplist_category_q5.pack()
    buttonb1 = Button(screen5, text="Tap", command= lambda: display_trend(categories))
    buttonb1.pack()
    button = Button(screen5, text="Quit", command=screen5.destroy)
    button.pack(side=BOTTOM)
    
    
def display_teen_mature_graph(required_contents, required_installs, teen_install, mature_install) :
    global screen10_1
    screen10_1 = Tk()
    screen10_1.title('Question-10.1')
    adjustWindow(screen10_1)
    #set(style="darkgrid")
    f, ax = subplots(figsize=(9, 7))
    Label(screen10_1, text="Ratio of downloads for for the app that qualifies as teen versus mature17+: {} that is {}".format(Fraction(teen_install/mature_install).limit_denominator(), teen_install/mature_install), fg='black').pack() 
    title('Teen vs Mature17+')
    rects = bar(required_contents,required_installs, color=['red','blue'])
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.01*height,'%.1f' % float(height),ha='center', va='bottom')
    xlabel('Contents')
    ylabel('Installs')
    show()
    canvas = FigureCanvasTkAgg(f, screen10_1) 
    canvas.draw()
    canvas.get_tk_widget().pack(side = TOP, fill = BOTH, expand = True)    
    button = Button(screen10_1, text="Quit", command=screen10_1.destroy)
    button.pack(side=BOTTOM)

def question_10() :
    global screen10
    screen10 = Tk()
    screen10.title('Question-10')
    adjustWindow(screen10)
    installs = data_naren['Installs']
    dates = data_naren['Last Updated']
    default_months = ['January','February','March','April','May','June','July','August','September','October','November','December']
    category = data_naren['Category']
    content_rating = data_naren['Content Rating']
    teen_install = 0
    mature_install = 0
    months = []
    cat_list = []
    install_list = []
    dum = []
    content_rating_list = []
    max_install_list = []
    category_list = []
    for content in content_rating :
        content_rating_list.append(content)
    for cat in category :
        if cat not in category_list :
            category_list.append(cat)
        cat_list.append(cat)
    for date in dates :
        month = date[0:-8].split()
        months.append(month)
    for install in installs :
        if install == 'Free' :
            install_list.append(0)
        else :
            install_list.append(int(install))
    for month in default_months :
        sum_of_installs = 0
        for cat in category_list :
            for i in range(len(install_list)) :
                dum = [month]
                if cat == cat_list[i] and dum == months[i]:
                    sum_of_installs += install_list[i]
        max_install_list.append(sum_of_installs)
    default_month_initials = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    for i in range(len(content_rating_list)) :
        if content_rating_list[i] == 'Teen' :        
            teen_install += install_list[i]
        if content_rating_list[i] == 'Mature 17+' :
            mature_install += install_list[i]
    print(teen_install/mature_install)
    required_contents = ['Teen','Mature 17+']
    required_installs = [teen_install, mature_install]
    #set(style="darkgrid")
    f, ax = subplots(figsize=(9, 7))
    button = Button(screen10, text="Teen vs Mature17+", command= lambda: display_teen_mature_graph(required_contents, required_installs, teen_install, mature_install))
    button.pack()
    title('Month that has seen the maximum downloads for each category', size=20)
    rects = bar(default_month_initials,max_install_list, color=(0.2, 0.4, 0.6, 0.6))
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.01*height,'%.1f' % float(height),ha='center', va='bottom')
    xlabel('Months')
    ylabel('Installs')
    show()
    canvas = FigureCanvasTkAgg(f, screen10) 
    canvas.draw()
    canvas.get_tk_widget().pack(side = TOP, fill = BOTH, expand = True)    
    button = Button(screen10, text="Quit", command=screen10.destroy)
    button.pack(side=BOTTOM)
    
def display_year_quarters(result, year_list, quarters, install_count_list) :
    global screen11_1
    screen11_1 = Tk()
    screen11_1.title('Question-11.1')
    adjustWindow(screen11_1)
    #set(style="darkgrid")
    f, ax = subplots(figsize=(9, 7))
    Label(screen11_1, text= 'Result --> Year : '+str(result[2])+', Quarter : '+str(result[1])+', Installs : '+str(result[0]), font=("Open Sans", 15, 'bold'), fg='black').pack() 
    title(year_list[0], size=20)
    rects = bar(quarters, install_count_list[0], color = ['red','blue','green','yellow'])
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.01*height,'%.1f' % float(height),ha='center', va='bottom')
    xlabel('Quarters')
    ylabel('Installs')
    show()
    canvas = FigureCanvasTkAgg(f, screen11_1) 
    canvas.draw()
    canvas.get_tk_widget().pack(side = TOP, fill = BOTH, expand = True)    
    button = Button(screen11_1, text="Quit", command=screen11_1.destroy)
    button.pack(side=BOTTOM)

def question_11() :
    global screen11
    screen11 = Tk()
    screen11.title('Question-11')
    adjustWindow(screen11)
    dates = data_naren['Last Updated']
    installs = data_naren['Installs']    
    install_list = []
    months = []
    years = []
    year_list = []
    date_list = []
    result = []
    install_count_list= []
    dictionary_year_quarter = {}
    first_quarter = [['January'], ['February'], ['March']]
    second_quarter = [['April'], ['May'], ['June']]
    third_quarter = [['July'], ['August'], ['September']]
    fourth_quarter = [['October'], ['November'], ['December']]
    for date in dates :
        date_list.append(date)
    for install in installs :
        if install == 'Free' :
            install_list.append(0)
        else :
            install_list.append(int(install))
    for date in date_list :
        years.append(date[-4:])
        month = date[0:-8].split()
        months.append(month)
    for year in years :
        if year not in year_list :
            year_list.append(year)
    for i in range(len(year_list)) :
        p = 0
        q = 0
        r = 0
        s = 0
        for j in range(len(date_list)) :
            if year_list[i] == date_list[j][-4:] :
                if months[j] in first_quarter :
                    p += install_list[j]
                if months[j] in second_quarter :
                    q += install_list[j]
                if months[j] in third_quarter :
                    r += install_list[j]
                if months[j] in fourth_quarter :
                    s += install_list[j]
        install_count = [p, q, r, s]
        dictionary_year_quarter.update({max(install_count) : [install_count.index(max(install_count)) , year_list[i]]})
        install_count_list.append(install_count)
    quarters = ['First','Second','Third','Fourth']  
    values_list = dictionary_year_quarter.keys()
    max_val = max(values_list)
    for key, values in dictionary_year_quarter.items() :
        if max_val == key :
            inst = key
            quart = values[0]
            yr = values[1]
    result.append(inst)
    result.append(quarters[quart])
    result.append(yr)
    #set(style="darkgrid")
    f, ax = subplots(figsize=(9, 7))
    button = Button(screen11, text="Result", command= lambda: display_year_quarters(result, year_list, quarters, install_count_list))
    button.pack()
    for k in range(1, len(install_count_list)+1) :     
        subplot(4, 3, k)
        title(year_list[k-1], size=20)
        bar(quarters, install_count_list[k-1])
        xlabel('Quarters')
        ylabel('Installs')
        tight_layout()
    show()
    canvas = FigureCanvasTkAgg(f, screen11) 
    canvas.draw()
    canvas.get_tk_widget().pack(side = TOP, fill = BOTH, expand = True)    
    button = Button(screen11, text="Quit", command=screen11.destroy)
    button.pack(side=BOTTOM)

def display_install(sports_install, sports_date, entertainment_install, entertainment_date, social_install, social_date, news_install, news_date, events_install, events_date, travel_install, travel_date, game_install, game_date) :
    global caught_year_variable, display_variable
    display_variable = StringVar()
    caught_year_variable = StringVar()
    caught_year_variable = entry_variable.get()
    get_category = predict_category_variable.get()
    if get_category == '--Select Category--' or caught_year_variable == '' :
        messagebox.showerror("Error", "Please fill in all the details!", parent=screen8_1)
    else :
        reg = LinearRegression()
        if get_category == 'SPORTS' :
            reg.fit(sports_date,sports_install)
        elif get_category == 'ENTERTAINMENT' :
            reg.fit(entertainment_date,entertainment_install)
        elif get_category == 'SOCIAL' :
            reg.fit(social_date,social_install)
        elif get_category == 'NEWS_AND_MAGAZINES' :
            reg.fit(news_date, news_install)
        elif get_category == 'EVENTS' :
            reg.fit(events_date, events_install)
        elif get_category == 'TRAVEL_AND_LOCAL' :
            reg.fit(travel_date,travel_install)
        elif get_category == 'GAME' :
            reg.fit(game_date, game_install)
        display_variable = float(caught_year_variable) * reg.coef_[0][0] + reg.intercept_[0]
        install_text.insert(END, str(display_variable)+' --> '+get_category+' --> '+ caught_year_variable+'\n')

def predict_install(sports_install, sports_date, entertainment_install, entertainment_date, social_install, social_date, news_install, news_date, events_install, events_date, travel_install, travel_date, game_install, game_date) :
    global screen8_1, install_text, entry_variable, predict_category_variable    
    entry_variable = StringVar()
    screen8_1 = Tk()
    screen8_1.title('Question-8.1')
    adjustWindow(screen8_1)
    predict_list = ['SPORTS','ENTERTAINMENT','SOCIAL','NEWS_AND_MAGAZINES','EVENTS','TRAVEL_AND_LOCAL','GAME']
    predict_category_variable = StringVar(screen8_1)
    droplist_predict_category = OptionMenu(screen8_1, predict_category_variable, *predict_list) 
    predict_category_variable.set('--Select Category--') 
    droplist_predict_category.config(width=30) 
    droplist_predict_category.pack()
    Label(screen8_1, text="Enter the year", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).pack()
    entry_variable = Entry(screen8_1)
    entry_variable.pack()
    year_button = Button(screen8_1, text="Predict", command= lambda: display_install(sports_install, sports_date, entertainment_install, entertainment_date, social_install, social_date, news_install, news_date, events_install, events_date, travel_install, travel_date, game_install, game_date))
    year_button.pack()
    install_text = Text(screen8_1, height=30, width=100)
    install_text.pack()
    button = Button(screen8_1, text="Quit", command=screen8_1.destroy)
    button.pack(side=BOTTOM)
    
def reshape_function(x, y) :
    x = array(x)
    x = x.reshape(-1,1)
    y = array(y)
    y = y.reshape(-1,1)
    return x, y

def perform_regression(x,y) :
    reg = LinearRegression()
    reg.fit(y,x)
    predictions = reg.predict(y)
    return predictions 

def calculate_rsquared(x,y) :
    X2 = add_constant(x)
    est = OLS(y,X2)
    est2 = est.fit()
    return est2.rsquared

def question_8() :
    global screen8
    screen8 = Tk()
    screen8.title('Question-8')
    adjustWindow(screen8)
    installs = data_naren['Installs']
    category = data_naren['Category'] 
    dates = data_naren['Last Updated']
    cat_list = []
    install_list = []
    category_sum_list = []
    date_list = []
    required_install_list = []
    required_date_list = []
    sports_install_list = []
    sports_date_list = []
    entertainment_install_list = []
    entertainment_date_list = []
    social_install_list = []
    social_date_list = []
    news_install_list = []
    news_date_list = []
    events_install_list = []
    events_date_list = []
    travel_install_list = []
    travel_date_list = []
    game_install_list = []
    game_date_list = []
    for date in dates :
        date_list.append(date)
    for cat in category :
        cat_list.append(cat)
    for install in installs :
        if install == 'Free' :
            install_list.append(0)
        else :
            install_list.append(int(install))
    required_category_list = ['SPORTS','ENTERTAINMENT','SOCIAL','NEWS_AND_MAGAZINES','EVENTS','TRAVEL_AND_LOCAL','GAME']
    for req in required_category_list :
        category_sum = 0
        for i in range(len(cat_list)) :
            if cat_list[i] == req :
                category_sum += install_list[i]
        category_sum_list.append(category_sum)
    for req in required_category_list :
        for i in range(len(install_list)) :
            if req == cat_list[i] :
                required_install_list.append(install_list[i])
                required_date_list.append(int(date_list[i][-4:]))
    for i in range(len(install_list)) :
        if cat_list[i] == 'SPORTS' :
            sports_install_list.append(install_list[i])
            sports_date_list.append(int(date_list[i][-4:]))
        elif cat_list[i] == 'ENTERTAINMENT' :
            entertainment_install_list.append(install_list[i])
            entertainment_date_list.append(int(date_list[i][-4:]))
        elif cat_list[i] == 'SOCIAL' :
            social_install_list.append(install_list[i])
            social_date_list.append(int(date_list[i][-4:]))
        elif cat_list[i] == 'NEWS_AND_MAGAZINES' :
            news_install_list.append(install_list[i])
            news_date_list.append(int(date_list[i][-4:]))
        elif cat_list[i] == 'EVENTS' :
            events_install_list.append(install_list[i])
            events_date_list.append(int(date_list[i][-4:]))
        elif cat_list[i] == 'TRAVEL_AND_LOCAL' :
            travel_install_list.append(install_list[i])
            travel_date_list.append(int(date_list[i][-4:]))
        elif cat_list[i] == 'GAME' :
            game_install_list.append(install_list[i])
            game_date_list.append(int(date_list[i][-4:]))
    sports_install, sports_date = reshape_function(sports_install_list, sports_date_list)
    entertainment_install, entertainment_date = reshape_function(entertainment_install_list, entertainment_date_list)
    social_install, social_date = reshape_function(social_install_list, social_date_list)
    news_install, news_date = reshape_function(news_install_list, news_date_list)
    events_install, events_date = reshape_function(events_install_list, events_date_list)
    travel_install, travel_date = reshape_function(travel_install_list, travel_date_list)
    game_install, game_date = reshape_function(game_install_list, game_date_list)
    sports_predictions = perform_regression(sports_install, sports_date)
    entertaiment_predictions = perform_regression(entertainment_install, entertainment_date)
    social_predictions = perform_regression(social_install, social_date)
    news_predictions = perform_regression(news_install, news_date)
    events_predictions = perform_regression(events_install, events_date)
    travel_predictions = perform_regression(travel_install, travel_date)
    game_predictions = perform_regression(game_install, game_date)
    set(style="darkgrid")
    f, ax = subplots(figsize=(9, 7))
    button_pred = Button(screen8, text="Predict for future years", command= lambda: predict_install(sports_install, sports_date, entertainment_install, entertainment_date, social_install, social_date, news_install, news_date, events_install, events_date, travel_install, travel_date, game_install, game_date))
    button_pred.pack()
    Label(screen8, text="As the prediction line for TRAVEL is steeper than other categories, it is most-likely to be downloaded in the coming years!",font=("Open Sans", 11, 'bold'),  fg='black').pack() 
    subplot(2,4,1)
    title('Current scenario')
    barplot(x=required_category_list, y=category_sum_list).set(xlabel = 'Required Categories', ylabel = 'Downloads')
    subplot(2,4,2)
    title('Sports({:.4f})'.format(calculate_rsquared(sports_date, sports_install)))
    scatter(sports_date, sports_install, c='black')
    plot(sports_date,sports_predictions,c='red',linewidth=2)
    xlabel('Years')
    ylabel('Installs')
    subplot(2,4,3)
    title('Entertainment({:.4f})'.format(calculate_rsquared(entertainment_date, entertainment_install)))
    scatter(entertainment_date, entertainment_install, c='black')
    plot(entertainment_date,entertaiment_predictions,c='red',linewidth=2)
    xlabel('Years')
    ylabel('Installs')
    subplot(2,4,4)
    title('Social({:.4f})'.format(calculate_rsquared(social_date, social_install)))
    scatter(social_date, social_install, c='black')
    plot(social_date,social_predictions,c='red',linewidth=2)
    xlabel('Years')
    ylabel('Installs')
    subplot(2,4,5)
    title('News({:.4f})'.format(calculate_rsquared(news_date, news_install)))
    scatter(news_date, news_install, c='black')
    plot(news_date,news_predictions,c='red',linewidth=2)
    xlabel('Years')
    ylabel('Installs')
    subplot(2,4,6)
    title('Events({:.4f})'.format(calculate_rsquared(events_date, events_install)))
    scatter(events_date, events_install, c='black')
    plot(events_date,events_predictions,c='red',linewidth=2)
    xlabel('Years')
    ylabel('Installs')
    subplot(2,4,7)
    title('Travel({:.4f})'.format(calculate_rsquared(travel_date, travel_install)))
    scatter(travel_date, travel_install, c='black')
    plot(travel_date,travel_predictions,c='red',linewidth=2)
    xlabel('Years')
    ylabel('Installs')
    subplot(2,4,8)
    title('Game({:.4f})'.format(calculate_rsquared(game_date, game_install)))
    scatter(game_date, game_install, c='black')
    plot(game_date,game_predictions,c='red',linewidth=2)
    xlabel('Years')
    ylabel('Installs')
    show()
    canvas = FigureCanvasTkAgg(f, screen8) 
    canvas.draw()
    canvas.get_tk_widget().pack(side = TOP, fill = BOTH, expand = True)  
    button2 = Button(screen8, text="Quit", command=screen8.destroy)
    button2.pack(side=BOTTOM)  

def question_17() :
    global screen17
    screen17 = Tk()
    screen17.title('Question-17')
    adjustWindow(screen17)
    f, ax = subplots(figsize=(9, 7))        
    regplot(x="Size", y="Installs", color = 'darkslategray',data=data_naren);
    title('Size vs Installs', size=20)
    xlabel("Size (in MB)")    
    show()
    canvas = FigureCanvasTkAgg(f, screen17) 
    canvas.draw()
    canvas.get_tk_widget().pack(side = TOP, fill = BOTH, expand = True)    
    button = Button(screen17, text="Quit", command=screen17.destroy)
    button.pack(side=BOTTOM)

main_screen()



