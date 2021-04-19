from tkinter import *
from tkinter import messagebox
import re , pymysql
from tkinter import Tk
from PIL import ImageTk, Image 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


def new():
    plt.title("THE PERCENTAGE OF DOWNLOADS CATEGORY WISE")
    plt.xticks(rotation=90)
    sns.countplot(data_naren['Category'],label='percentage')
    plt.show()


# This function is used for adjusting window size and making the necessary configuration on start of window 
def adjustWindow(window): 
    w = 600  # width for the window size 
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
    w = 600  # width for the window size 
    h = 600  # height for the window size 
    ws = screen.winfo_screenwidth()  # width of the screen 
    hs = screen.winfo_screenheight()  # height of the screen 
    x = (ws/2) - (w/2)  # calculate x and y coordinates for the Tk window 
    y = (hs/2) - (h/2) 
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
    screen1.title("Registeration") 
    adjustWindow(screen1) # configuring the window 
    Label(screen1, text="Registration Form", width='42', height="2", font=("Calibri", 22, 'bold'), fg='white', bg='#d9660a').place(x=0, y=0) 
   #Label(screen1, text="", bg='#174873', width='55', height='30').place(x=105, y=100) 
    
    photo = PhotoImage(file="rf.png") # opening left side image - Note: If image is in same folder then no need to mention the full path 
    label = Label(screen1, image=photo, text="") # attaching image to the label 
    label.place(x=0, y=80) 
    label.image = photo # it is necessary in Tkinter to keep a instance of image to display image in label 
      
    
    Label(screen1, text="Full Name:", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=250, y=130) 
    Entry(screen1, textvar=fullname).place(x=380, y=130) 
    Label(screen1, text="Email ID:", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=250, y=180) 
    Entry(screen1, textvar=email).place(x=380, y=180) 
    Label(screen1, text="Country:", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=250, y=230) 
    Radiobutton(screen1, text="India", variable=country, value=1,fg='white', bg='#174873').place(x=380, y=230)     
    Radiobutton(screen1, text="Other", variable=country, value=2,fg='white', bg='#174873').place(x=450, y=230) 
                    
    Label(screen1, text="gender:", font=("Open Sans", 11, 'bold'), fg='white', bg='#174873', anchor=W).place(x=250, y=280) 
    #list1 = ['Andhra Pradesh','Arunachal Pradesh ','Assam','Bihar','Chhattisgarh','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu and Kashmir','Jharkhand','Karnataka','Kerala','Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Rajasthan','Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal','Andaman and Nicobar Islands','Chandigarh','Dadra and Nagar Haveli','Daman and Diu','Lakshadweep','National Capital Territory of Delhi','Puducherry'] 
    list1 = ['Male','Female','Other']
    droplist = OptionMenu(screen1, gender, *list1) 
    droplist.config(width=18) 
    gender.set('--select your gender--') 
    droplist.place(x=380, y=275) 
    Label(screen1, text="Password:", font=("Open Sans", 11, 'bold'), fg='white',bg='#174873', anchor=W).place(x=250, y=330) 
    Entry(screen1, textvar=password, show="*").place(x=380, y=330) 
    Label(screen1, text="Re-Password:", font=("Open Sans", 11, 'bold'), fg='white',bg='#174873', anchor=W).place(x=250, y=380) 
    entry_4 = Entry(screen1, textvar=repassword, show="*") 
    entry_4.place(x=380, y=380) 
    Checkbutton(screen1, text="I accept all terms and conditions", variable=tnc, bg='#174873', font=("Open Sans", 9, 'bold'), fg='brown').place(x=275, y=430) 
    Button(screen1, text='Submit', width=20, font=("Open Sans", 13, 'bold'), bg='brown', fg='black',command=register_user).place(x=270, y=480)              
    
    

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
    Label(screen2, text="Welcome " + registration_info[0][1], width='42', height="2", font=("Calibri", 22, 'bold'), fg='white', bg='#d9660a').place(x=0, y=0) 
    Label(screen2, text="", bg='#174873', width='20', height='20').place(x=0, y=96) 
    #Message(screen2, text='" Some people dream of accomplishing great things. Others stay awake and make it happen. "\n\n - By Some Night Owl', width='180', font=("Helvetica", 10, 'bold', 'italic'), fg='white', bg='#174873', anchor = CENTER).place(x=10, y=100) 
    
    photo = PhotoImage(file="bft.png") # opening left side image - Note: If image is in same folder then no need to mention the full path 
    label = Label(screen2, image=photo, text="") # attaching image to the label 
    label.place(x=10, y=270) 
    label.image = photo # it is necessary in Tkinter to keep a instance of image to display image in label 
    
    photo1 = PhotoImage(file="bf.png") # opening right side image - Note: If image is in same folder then no need to mention the full path 
    label1 = Label(screen2, image=photo1, text="") # attaching image to the label 
    label1.place(x=200, y=96) 
    label1.image = photo1 # it is necessary in Tkinter to keep a instance of image to display image in label 
    
    Button(screen2, text='Fetch Record', width=20,height=4, font=("Open Sans", 13, 'bold'), bg='brown', fg='white').place(x=270, y=150) 
    Button(screen2, text='Insert Record', width=20,height=4, font=("Open Sans", 13, 'bold'), bg='brown', fg='white').place(x=270, y=250) 
    Button(screen2, text='Perform Function', width=20,height=4, font=("Open Sans", 13, 'bold'), bg='brown', fg='white',command=next_page).place(x=270, y=350)
    
    
def next_page():    
    global screen3 
    screen3 = Toplevel(screen) 
    screen3.title("BRUTE FORCE")
    adjustWindow1(screen3)
    Label(screen3, text="Enter New Record", width='31', height="2", font=("Calibri", 22, 'bold'), fg='white', bg='#d9660a').pack()
    Button(screen3, text='1 Funct', width=20, font=("Open Sans", 13, 'bold'), bg='brown', fg='white',command=func1).place(x=270, y=350)
    

def main_screen():
    global screen, username_verify, password_verify
    screen = Tk()
    username_verify = StringVar()
    password_verify = StringVar()
    screen.title("BRUTE FORCE")
    adjustWindow(screen)
    
    img2 = ImageTk.PhotoImage(Image.open("edited.jpg"))  
    d1 = Label(image= img2) 
    d1.place(x =-1,y = 70)
    
    Label(screen,text="BRUTE FORCE Manager",width="500",height="2",font=("Calibri",22,'bold'),fg='white',bg='#d9660a').pack()
    Label(screen, text="Please enter details below to login", bg='#174873', fg='white').place(x=212,y=150) 
    Label(screen, text="Username * ", font=("Open Sans", 10, 'bold'), bg='#174873', fg='white').place(x=258,y=192)             
    Entry(screen, textvar=username_verify).place(x=237,y=215) 
    Label(screen, text="Password * ", font=("Open Sans", 10, 'bold'), bg='#174873', fg='white').place(x=258,y=262) 
    Entry(screen, textvar=password_verify, show="*").place(x=237,y=285) 
    Button(screen, text="LOGIN", bg="#e79700", width=15, height=1, font=("Open Sans", 13, 'bold'), fg='white', command=login_verify).place(x=220,y=325) 
    Button(screen, text="New User? Register Here", height="2", width="30", bg='#e79700', font=("Open Sans", 10, 'bold'), fg='white', command=register).place(x=170,y=380) 
    
    img1 = ImageTk.PhotoImage(Image.open("bft.png"))  
    c1 = Label(image= img1) 
    c1.place(x =50,y = 0) 
            
    screen.mainloop()
    
def func1():
    global screen4 
    screen4 = Toplevel(screen) 
    screen4.title("Function 1")
    adjustWindow1(screen4)
    data_naren=pd.read_csv("C:\\Datasets\\internshipdataset1.csv")
    
    #plt.title("THE PERCENTAGE OF DOWNLOADS CATEGORY WISE")
    #plt.xticks(rotation=90)
    #outbox = Canvas(screen4, width = 200, height = 200, bg = "light grey")
    #outbox.grid(row = 3, column = 0, sticky = W)
    #plot = sns.countplot(data_naren['Category'],label='percentage')
    #outbox.insert(plot) 
    
        
    plt.title("THE PERCENTAGE OF DOWNLOADS")
    plt.xticks(rotation=90)
    sns.countplot(data_naren['Android Ver'],label='percentage')
    plt.show()
    
    plt.savefig('C:\\Datasets\\svm_conf.jpg', dpi=100)
    #plt.show()
'''
    f=Figure(figsize=(5,5),dpi=100)
    a=f.add_subplot(111)
    a.sns.countplot(data_naren['Category'],label='percentage')
    canvas=FigureCanvasTkAgg(f)
    canvas.show()
    canvas.get_tk_widget().pack(side=tk.TOP,fill=tk.BOTH,expand=True)
     '''
 
    
main_screen()    