from tkinter import *
import tkinter.messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
import numpy as np
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="Durai",
  password="Pass",
  database="pypro"
)

mycursor = mydb.cursor()

def Open():
          global root
          root.destroy()
          import Updator
          Updator.up()
def fetchforbars(s):
    mycursor.execute("Select COUNT(No) from lst")
    r=mycursor.fetchall()
    LT=[]
    sum=0
    if s=="Month":
        for i in range(1,r[0][0]+1):
            mycursor.execute("Select Sum(Cost) from log where No="+str(i)+" and MONTH(Dates)= MONTH(CURDATE()) and YEAR(Dates)=Year(CURDATE()) ")
            r=mycursor.fetchall()
            if r[0][0]==None:
                LT.append(0)
            else:
                LT.append(int(r[0][0]))
                sum+=int(r[0][0])
    elif s=="Today":
        for i in range(1,r[0][0]+1):
            mycursor.execute("Select Sum(Cost) from log where No="+str(i)+" and Day(Dates)= Day(CURDATE()) and MONTH(Dates)= MONTH(CURDATE()) and YEAR(Dates)=Year(CURDATE()) ")
            r=mycursor.fetchall()
            if r[0][0]==None:
                LT.append(0)
            else:
                LT.append(int(r[0][0]))
                sum+=int(r[0][0])
    if s=="Yesterday":
        for i in range(1,r[0][0]+1):
            mycursor.execute("Select Sum(Cost) from log where No="+str(i)+" and Day(Dates)= Day(CURDATE())-1 and  MONTH(Dates)= MONTH(CURDATE()) and YEAR(Dates)=Year(CURDATE()) ")
            r=mycursor.fetchall()
            if r[0][0]==None:
                LT.append(0)
            else:
                LT.append(int(r[0][0]))
                sum+=int(r[0][0])
    if s=="Year":
        for i in range(1,r[0][0]+1):
            mycursor.execute("Select Sum(Cost) from log where No="+str(i)+" and YEAR(Dates)=Year(CURDATE()) ")
            r=mycursor.fetchall()
            if r[0][0]==None:
                LT.append(0)
            else:
                LT.append(int(r[0][0]))
                sum+=int(r[0][0])                        
    return (LT)
def fetchforpie(s):
    mycursor.execute("Select COUNT(No) from lst")
    r=mycursor.fetchall()
    LT=[]
    LST=[]
    sum=0
    if s=="Month":
        for i in range(1,r[0][0]+1):
            mycursor.execute("Select Sum(Cost) from log where No="+str(i)+" and MONTH(Dates)= MONTH(CURDATE()) and YEAR(Dates)=Year(CURDATE()) ")
            r=mycursor.fetchall()
            if r[0][0]==None:
                LT.append(0)
            else:
                LT.append(int(r[0][0]))
                sum+=int(r[0][0])
    elif s=="Today":
        for i in range(1,r[0][0]+1):
            mycursor.execute("Select Sum(Cost) from log where No="+str(i)+" and Day(Dates)= Day(CURDATE()) and MONTH(Dates)= MONTH(CURDATE()) and YEAR(Dates)=Year(CURDATE()) ")
            r=mycursor.fetchall()
            if r[0][0]==None:
                LT.append(0)
            else:
                LT.append(int(r[0][0]))
                sum+=int(r[0][0])
    if s=="Yesterday":
        for i in range(1,r[0][0]+1):
            mycursor.execute("Select Sum(Cost) from log where No="+str(i)+" and Day(Dates)= Day(CURDATE())-1 and  MONTH(Dates)= MONTH(CURDATE()) and YEAR(Dates)=Year(CURDATE()) ")
            r=mycursor.fetchall()
            if r[0][0]==None:
                LT.append(0)
            else:
                LT.append(int(r[0][0]))
                sum+=int(r[0][0])
    if s=="Year":
        for i in range(1,r[0][0]+1):
            mycursor.execute("Select Sum(Cost) from log where No="+str(i)+" and YEAR(Dates)=Year(CURDATE()) ")
            r=mycursor.fetchall()
            if r[0][0]==None:
                LT.append(0)
            else:
                LT.append(int(r[0][0]))
                sum+=int(r[0][0])                
    indi=[]
    LST=list(LT)
    k=0
    #print(LST)
    for i in range(len(LT)):
        if LT[i]<sum/100:
            indi.append(i)
            LST.pop(i-k)
            k+=1
    #print(LST,indi)        
    return (LST,indi)
def ffp2(indi):
    mycursor.execute("Select Name from lst")
    r=mycursor.fetchall()
    LST=[]
    for i in range(len(r)):
        if i in indi:
            pass
        else:
            LST.append(r[i][0])
    #print(LST)    
    return LST
def chocobar(s):
    global frame3
    frame3.destroy()
    frame3= Frame(frameb,background="#FFFFFF")
    fig = Figure(figsize = (6, 3),dpi = 100)
    v=fetchforbars(s)
    mycursor.execute("Select Name from lst")
    r=mycursor.fetchall()
    LST=[]
    for i in range(len(r)):
        LST.append(r[i][0])
    LST=  np.array(LST)
    y = np.array(v)
    try:
        plot1 = fig.add_subplot(111)
        c = ['red', 'yellow', 'green', 'blue', 'orange']
        plot1.bar(LST,y,color=c,width=0.4)         
        canvas = FigureCanvasTkAgg(fig,master = frame3)  
        canvas.draw()
      
        canvas.get_tk_widget().pack()
      
        #toolbar = NavigationToolbar2Tk(canvas,frame2)
        #toolbar.update()
      
        #canvas.get_tk_widget().pack()
    except:
        fig = Figure(figsize = (0, 0),dpi = 100)
        canvas = FigureCanvasTkAgg(fig,master = frame3)  
        canvas.draw()
      
        canvas.get_tk_widget().pack()
    frame3.pack()
def chocobar1():
    fig = Figure(figsize = (6, 3),dpi = 100)
    v=fetchforbars("Month")
    mycursor.execute("Select Name from lst")
    r=mycursor.fetchall()
    LST=[]
    for i in range(len(r)):
        LST.append(r[i][0])
    LST=  np.array(LST)
    y = np.array(v)
    try:
        plot1 = fig.add_subplot(111)
        c = ['red', 'yellow', 'green', 'blue', 'orange']
        plot1.bar(LST,y,width=0.4,color=c)         
        canvas = FigureCanvasTkAgg(fig,master = frame3)  
        canvas.draw()
      
        canvas.get_tk_widget().pack()
      
        #toolbar = NavigationToolbar2Tk(canvas,frame2)
        #toolbar.update()
      
        #canvas.get_tk_widget().pack()
    except:
        fig = Figure(figsize = (0, 0),dpi = 100)
        canvas = FigureCanvasTkAgg(fig,master = frame3)  
        canvas.draw()
      
        canvas.get_tk_widget().pack()
    frame3.pack()     
def plot(s):
    global frame2
    frame2.destroy()
    frame2= Frame(framep,background="#FFFFFF")
    fig = Figure(figsize = (5, 5),dpi = 100)
    v=fetchforpie(s)
    lbl=ffp2(v[1])
    y = np.array(v[0])
    try:
        plot1 = fig.add_subplot(111)
        plot1.pie(y,labels=lbl)         
        canvas = FigureCanvasTkAgg(fig,master = frame2)  
        canvas.draw()
      
        canvas.get_tk_widget().pack()
      
        #toolbar = NavigationToolbar2Tk(canvas,frame2)
        #toolbar.update()
      
        #canvas.get_tk_widget().pack()
    except:
        fig = Figure(figsize = (0, 0),dpi = 100)
        canvas = FigureCanvasTkAgg(fig,master = frame2)  
        canvas.draw()
      
        canvas.get_tk_widget().pack()
    frame2.pack()    
def plot1():
    
    fig = Figure(figsize = (5, 5),dpi = 100)
    v=fetchforpie("Month")
    lbl=ffp2(v[1])
    y = np.array(v[0])
    print(y)
    try:
        plot1 = fig.add_subplot(111)
        plot1.pie(y,labels=lbl)         
        canvas = FigureCanvasTkAgg(fig,master = frame2)  
        canvas.draw()
      
        canvas.get_tk_widget().pack()
      
        #toolbar = NavigationToolbar2Tk(canvas,frame2)
        #toolbar.update()
      
        #canvas.get_tk_widget().pack()
    except:
        fig = Figure(figsize = (0, 0),dpi = 100)
        canvas = FigureCanvasTkAgg(fig,master = frame2)  
        canvas.draw()
      
        canvas.get_tk_widget().pack()
def text():
    numbers=fetchforbars("Month")
    mycursor.execute("Select Name from lst")
    r=mycursor.fetchall()
    names=[]
    for i in range(len(r)):
        names.append(r[i][0])
    for i in range(len(names)):
        Label(frame4, text=str(names[i]), font=('Ariel',18,'bold'),bg="#FFFFFF").grid(row=i,column=0,sticky="W",pady=10)
        Label(frame4, text=str(numbers[i]), font=('Ariel',18,'normal'),bg="#FFFFFF",justify="left",fg="#FF69B4").grid(row=i,column=1)
def text1(s):
    global frame4
    frame4.destroy()
    frame4=Frame(framet,background="#FFFFFF")
    numbers=fetchforbars(s)
    mycursor.execute("Select Name from lst")
    r=mycursor.fetchall()
    names=[]
    for i in range(len(r)):
        names.append(r[i][0])
    for i in range(len(names)):
        Label(frame4, text=str(names[i]), font=('Ariel',18,'bold'),bg="#FFFFFF").grid(row=i,column=0,sticky="W",pady=10)
        Label(frame4, text=str(numbers[i]), font=('Ariel',18,'normal'),bg="#FFFFFF",justify="left",fg="#FF69B4").grid(row=i,column=1)
    frame4.pack()    
root = Tk()  
root.title('Plotting in Tkinter')
  
root.geometry("500x500")
root.configure(bg='#FFFFFF')

frame = Frame(root,height=20,width=200,background="#FFFFFF") 
Label(frame, text="Money Manager", font=('Vladimir Script',25,'bold'),bg="#FFFFFF",fg='#00FFFF').pack(anchor='w')
frame.pack(fill=X,padx=20,pady=5)

masterframe=Frame(root,background='#FFFFFF')
frameg = Frame(masterframe,background='#FFFFFF')
framep = Frame(frameg,background='#FFFFFF')
frame_1 = Frame(framep,background='#FFFFFF')
Option_pie= tkinter.StringVar(root)
Option_pie.set('Month')
L1=['Today','Yesterday','Month','Year']
option_menu = OptionMenu(frame_1,Option_pie,*L1,command= plot)
option_menu.config(bg="#FFFFFF")
option_menu.config(fg="#000000",height=1)
option_menu.config(activeforeground="#4169E1",activebackground="#FFFFFF",highlightthickness=2,relief='flat',highlightcolor="#4169E1",font=('Ariel',8,'normal'))
option_menu['menu'].config(bg="#FFFFFF",activebackground="#4169E1")
option_menu.grid(row=0,column=0,pady=9,padx=8,sticky='e')
option_menu.pack()
frame_1.pack()


frame2= Frame(framep,background="#FFFFFF")
plot1()
frame2.pack()
framep.pack()

frameb = Frame(frameg,background='#FFFFFF')
frame_2 = Frame(frameb,background='#FFFFFF')
Option_bar= tkinter.StringVar(root)
Option_bar.set('Month')
L1=['Today','Yesterday','Month','Year']
option_menu = OptionMenu(frame_2,Option_bar,*L1,command= chocobar)
option_menu.config(bg="#FFFFFF")
option_menu.config(fg="#000000",height=1)
option_menu.config(activeforeground="#4169E1",activebackground="#FFFFFF",highlightthickness=2,relief='flat',highlightcolor="#4169E1",font=('Ariel',8,'normal'))
option_menu['menu'].config(bg="#FFFFFF",activebackground="#4169E1")
option_menu.grid(row=0,column=0,pady=9,padx=8,sticky='e')
option_menu.pack()
frame_2.pack()


frame3= Frame(frameb,background="#FFFFFF")
chocobar1()
frame3.pack()
frameb.pack()
frameg.grid(row=0,column=0,sticky="w")


framet= Frame(masterframe,background="#FFFFFF")

frame_3 = Frame(framet,background='#FFFFFF')
Option_text= tkinter.StringVar(root)
Option_text.set('Month')
L1=['Today','Yesterday','Month','Year']
option_menu = OptionMenu(frame_3,Option_text,*L1,command= text1)
option_menu.config(bg="#FFFFFF")
option_menu.config(fg="#000000",height=1)
option_menu.config(activeforeground="#4169E1",activebackground="#FFFFFF",highlightthickness=2,relief='flat',highlightcolor="#4169E1",font=('Ariel',8,'normal'))
option_menu['menu'].config(bg="#FFFFFF",activebackground="#4169E1")
option_menu.grid(row=0,column=0,pady=9,padx=8,sticky='e')
option_menu.pack()
frame_3.pack()

frame4= Frame(framet,background="#FFFFFF")
text()
frame4.pack()
framet.grid(row=0,column=1,padx=100)
Butt = Button(masterframe, text="Update",relief='flat',font=('Ariel',8,'bold'), command=Open,width=12,height=1,bg="#00FFFF",fg="#FFFFFF",activebackground="#FFFFFF",activeforeground="#00FFFF").grid(row=1,column=0)
masterframe.pack()
#plot_button = Button(master = root,height = 2,command=plot,width = 10,text = "Plot")
#plot_button.pack()

root.mainloop()
