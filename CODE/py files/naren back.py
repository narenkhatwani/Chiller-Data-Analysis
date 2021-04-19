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

data_naren=pd.read_csv("C:\\Datasets\\internshipdataset1.csv")
data_harsh=pd.read_csv("C:\\Datasets\\internshipdataset1.csv")
data_priya=pd.read_csv("C:\\Datasets\\Dataset2.csv")

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
    Button(screen3, text="1) What is the percentage download in each category on the playstore.",width=70, height=2, bg='brown', fg='white',font=("Open Sans", 10, 'bold'),command=function1).place(x=80,y=84)
    #Button(screen3, text='Function 2', width=15, height=1,font=("Open Sans", 15, 'bold'), bg='brown', fg='black').place(x=800, y=175)              
    Button(screen3, text="""2) How many apps have managed to get the following number of downloads a) Between 10,000 and 50,000         
    b) Between 50,000 and 150000 c) Between 150000 and 500000 d) Between 500000 and 5000000 e) More than 5000000""",width=95, height=2, bg='brown', fg='white',font=("Open Sans", 10, 'bold')).place(x=80,y=166)
    #Button(screen3, text='3', width=1, height=1,font=("Open Sans", 15, 'bold'), bg='brown', fg='black').place(x=30, y=250)              
    Button(screen3, text="3) Which category of apps have managed to get the most,least and an average of 2,50,000 downloads atleast.",width=90, height=2,font=("Open Sans", 10, 'bold'), bg='brown', fg='white',command=question_3).place(x=80,y=248)
    Button(screen3, text="4) Which category of apps have managed to get the highest maximum average ratings from the users.",width=90, height=2,font=("Open Sans", 10, 'bold'), bg='brown', fg='white',command=question_4).place(x=80,y=332)
    Button(screen3, text="5) What is the download trend category wise over the period for which the data is being made available.",width=90, height=2,font=("Open Sans", 10, 'bold'), bg='brown', fg='white',command=function5).place(x=80,y=416)
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
    most likely to be downloaded in the coming years, kindly make a prediction and back it with suitable findings.""",width=95, height=2, bg='brown', fg='white',font=("Open Sans", 10, 'bold'),command=function8).place(x=80,y=164)
    Button(screen311, text="""9) All those apps who habve managed to get over 1,00,000 downloads, have they managed to get an average rating
    of 4.1 and above? An we conclude something in co-relation to the number of downloads and the ratings received.""",width=95, height=2, bg='brown', fg='white',font=("Open Sans", 10, 'bold'),command=function9).place(x=80,y=248)
    Button(screen311, text="""10) Across all the years ,which month has seen the maximum downloads fr each of the category. 
    What is the ratio of downloads for the app that qualifies as teen versus mature17+""",width=90, height=2,font=("Open Sans", 10, 'bold'), bg='brown', fg='white',command=function10).place(x=80,y=332)
    Button(screen311, text="11) Which quarter of which year has generated the highest number of install for each app used in the study?",width=90, height=2,font=("Open Sans", 10, 'bold'), bg='brown', fg='white').place(x=80,y=416)
    Button(screen311, text="""12) Which of all the apps given have managed to generate the most positive and negative sentiments.Also figure 
    out the app which has generated approximately the same ratio for positive and negative sentiments.""",width=90, height=2,font=("Open Sans", 10, 'bold'), bg='brown', fg='white').place(x=80,y=500)
    
    
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

    
    Button(screen312, text="13) Study and find out the relation between the Sentiment-polarity and sentiment-subjectivity of all the apps.",width=90, height=2,font=("Open Sans", 10, 'bold'), bg='brown', fg='white').place(x=80,y=84)
    Button(screen312, text="""14) Generate an interface where the client can see the reviews categorized as positive.negative and neutral 
    ,once they have selected the app from a list of apps available for the study.""",width=90, height=2,font=("Open Sans", 10, 'bold'), bg='brown', fg='white').place(x=80,y=164)
    
    Button(screen312, text="15) Is it advisable to launch an app like ’10 Best foods for you’? Do the users like these apps?",width=95, height=2, bg='brown', fg='white',font=("Open Sans", 10, 'bold')).place(x=80,y=248)
    Button(screen312, text="16) Which month(s) of the year , is the best indicator to the avarage downloads that an app will generate over the entire year?",width=90, height=2,font=("Open Sans", 10, 'bold'), bg='brown', fg='white').place(x=80,y=332)
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
 
def function8():
    global screen11 
    screen11 = Toplevel(screen) 
    screen11.title("FUNCTION 9")
    adjustWindow(screen11)
        #function8
    data_naren['Installs']=data_naren['Installs'].map(lambda x:x.rstrip('+'))
    data_naren['Installs']=data_naren['Installs'].map(lambda x:''.join(x.split(',')))
    
    #function8
    lb_make=LabelEncoder()
    
    data_naren['Category NUM']=lb_make.fit_transform(data_naren['Category'])
    print(data_naren['Category NUM'])
    X=data_naren[["Category NUM"]]
    #c=data1[data1['Category NUM'][1],data1['Category NUM'][4],data1['Category NUM'][20],data1['Category NUM'][8],data1['Category NUM'][16],data1['Category NUM'][24],data1['Category NUM'][30],data1['Category NUM'][28],data1['Category NUM'][12],data1['Category NUM'][18]]
    #X=data1[c]
    y=data_naren['Installs']
    
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.30,random_state=0)
    
    
    regressor=LinearRegression()
    regressor.fit(X_train,y_train)
    y_pred=regressor.predict(X_test)
    
    data1=pd.DataFrame({'Actual':y_test,'Predicted':y_pred})
    print(data1)
    
    plt.subplots(figsize=(6,6))
    plt.title("PREDICTION")
    plt.scatter(y_test,y_pred)
    plt.xlabel("DOWNLOADS")
    plt.ylabel("PREDICTED DOWNLOADS")
    plt.xticks(fontsize=6,rotation=90)
    plt.savefig('C:\\Users\\Admin\\Desktop\\internship gui\\function8.jpg',dpi=100)
    
    img = ImageTk.PhotoImage(Image.open('function8.jpg'))
    panel =Label(screen11, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")
        
    screen11.mainloop()
    
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
    
    
    

main_screen()    

#point 10

'''

    list24 = ['10 Best Foods for You','104 æ‰¾å·¥ä½œ - æ‰¾å·¥ä½œ æ‰¾æ‰“å·¥ æ‰¾å…¼è· å±¥æ·å¥æª¢ å±¥æ·è¨ºç™‚å®¤','11st','1800 Contacts - Lens Store','1LINE â€“ One Line with One Touch','2018Emoji Keyboard ðŸ˜‚ Emoticons Lite -sticker&amp;gif','21-Day Meditation Experience','2Date Dating App, Love and matching','2GIS: directory & navigator','2RedBeans','2ndLine - Second Phone Number','30 Day Fitness Challenge - Workout at Home','365Scores - Live Scores','3D Blue Glass Water Keyboard Theme','3D Color Pixel by Number - Sandbox Art Coloring','3D Live Neon Weed Launcher','4 in a Row','4K Wallpapers and Ultra HD Backgrounds','æ·é‹ã€è²·æˆ¿è³£æˆ¿è¡Œæƒ…ã€æˆ¿åƒ¹æˆ¿è²¸æŸ¥è©¢591æˆ¿å±‹äº¤æ˜“-ç§Ÿå±‹ã€ä¸å¤å±‹ã€æ–°å»ºæ¡ˆã','€å¯¦åƒ¹ç™»éŒ„ã€åˆ¥å¢…é€å¤©ã€å…¬å¯“å¥—æˆ¿ã€','591æˆ¿å±‹äº¤æ˜“-é¦™æ¸¯','7 Cups: Anxiety & Stress Chat','7 Day Food Journal Challenge','7 Minute Workout','7 Weeks - Habit & Goal Tracker','8 Ball Pool','850 Sports News Digest','8fit Workouts & Meal Planner','95Live -SG#1 Live Streaming App','A Call From Santa Claus!','A Manual of Acupuncture','A Word A Day','A&E - Watch Full Episodes of TV Shows','A+ Gallery - Photos & Videos','A+ Mobile','ABC Kids - Tracing & Phonics','ABC News - US & World News','ABC Preschool Free','ABCmouse.com','AC - Tips & News for Androidâ„¢','ACE Elite','AD - Nieuws, Sport, Regio & Entertainment','ADP Mobile Solutions','ADW Launcher 2','AMC Theatres','ANA','AOL - News, Mail & Video','AP Mobile - Breaking News','APE Weather ( Live Forecast)','APUS Launcher - Theme, Wallpaper, Hide Apps','ARY NEWS','ARY NEWS URDU','ASOS','ASUS Calling Screen','ASUS Cover for ZenFone 2','ASUS Quick Memo','ASUS Sound Recorder','ASUS SuperNote','AT&T Navigator: Maps, Traffic','AT&T Smart Wi-Fi','AT&T Visual Voicemail','AVG Cleaner â€“ Speed, Battery & Memory Booster','Abs Training-Burn belly fat','Account Manager','Accounting App - Zoho Books','AccuWeather: Daily Forecast & Live Weather Reports','Acorn TV: World-class TV from Britain and Beyond','Acorns - Invest Spare Change','Acupuncture Assistant','AdWords Express','Ada - Your Health Guide','Add Text To Photo','Adobe Acrobat Reader','Adobe Photoshop Express:Photo Editor Collage Maker','Adult Dating - AdultFinder','Adult Glitter Color by Number Book - Sandbox Pages','Advanced Task Killer','Agar.io','Age Calculator','Agoda â€“ Hotel Booking Deals','Air Traffic','AirAsia','AirBrush: Easy Photo Editor','Airbnb','Airport + Flight Tracker Radar','Airway Ex - Intubate. Anesthetize. Train.','Akinator','AlReader -any text book reader','Alarm Clock','Alarm Clock Free','Alfred Home Security Camera','AliExpress - Smarter Shopping, Better Living','All Email Providers','All Events in City','All Football - Latest News & Videos','All Football GO- Live Score, Games','All Language Translator Free','All Maths Formulas','All Mental disorders','All Social Networks','All Video Downloader 2018','All-In-One Toolbox: Cleaner, Booster, App Manager','All-in-One Mahjong 3 FREE','AllTrails: Hiking, Running & Mountain Bike Trails','Allegiant','Allrecipes Dinner Spinner']
    
    x1=data_priya.loc[(data_priya['App']==app_name.get())&(data_priya['Sentiment']=='Positive'),['App','Sentiment']].count()
    
    x2=data_priya.loc[(data_priya['App']==app_name.get())&(data_priya['Sentiment']=='Negative'),['App','Sentiment']].count()
    Label(screen25, text="Positive sentiments", bg='yellow', fg='black').pack()
    Label(screen25, text=x1, bg='yellow', fg='black').pack()
    Label(screen25, text="Negative sentiments", bg='yellow', fg='black').pack()
    Label(screen25, text=x2, bg='yellow', fg='black').pack()
    
    Label(screen25, text=x2, bg='yellow', fg='black').pack()
    


'''
