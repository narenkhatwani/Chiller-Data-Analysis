from tkinter import *
root=Tk()
root.geometry('500x500')
root.title("Registration form")

label_0=Label(root,text="Modify dataset 2",width=20,font=("bold",20))
label_0.place(x=90,y=53)

label_1=Label(root,text="App:",width=20,font=("bold",10))
label_1.place(x=80,y=130)

entry_1=Entry(root)
entry_1.place(x=240,y=130)

label_2=Label(root,text="Translated Review",width=20,font=("bold",10))
label_2.place(x=68,y=180)

entry_2=Entry(root)
entry_2.place(x=240,y=180)

label_3=Label(root,text="Sentiment",width=20,font=("bold",10))
label_3.place(x=70,y=230)
var=IntVar()
Radiobutton(root,text="Positive",padx=5,variable=var,value=1).place(x=210,y=230)
Radiobutton(root,text="Neutral",padx=20,variable=var,value=2).place(x=280,y=230)
Radiobutton(root,text="Negative",padx=20,variable=var,value=3).place(x=380,y=230)



label_5=Label(root,text="Sentiment Polarity",width=20,font=("bold",10))
label_5.place(x=85,y=350)
entry_3=Entry(root)
entry_3.place(x=240,y=350)

label_6=Label(root,text="Sentiment Subjectivity",width=20,font=("bold",10))
label_6.place(x=85,y=390)
entry_4=Entry(root)
entry_4.place(x=240,y=390)

Button(root,text='Enter Data',width=20,bg='brown',fg='white').place(x=180,y=450)


mainloop()