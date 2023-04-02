from tkinter import *
import tkinter.messagebox
import datetime
import time
import os
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="Durai",
  password="Pass",
  database="pypro"
)

mycursor = mydb.cursor()
def up():
  def ini():
    print("///")  
    mycursor.execute("SELECT * FROM lst")
    r=mycursor.fetchall()
    LIST=[]
    for i in r:
      if i[2]:
        LIST.append(i[1])
    return LIST  
  LIST=ini()    
  #LIST=['Food', 'Fuel','EB','TDS']
  #LIST_W=list(LIST)
  root=None
  f=0
  def Root():
      global photoimage 
      root = Tk()
      global l
      l="400x320"
      root.geometry(l)
      root.configure(bg='#FFFFFF')
      global k
      k=0
      def submit():
          global k
          f=0
          D=dict()
          for i in range(k):
              x=evalue[i].get()
              y_=value_inside[i].get()
              try:
                  if x=='Select':
                      break
                  else:
                      if isinstance(eval(x), int):
                          D[y_]=x
              except:
                  if f==0:
                      tkinter.messagebox.showinfo("Invalid Input!",  "Please enter an Integer")
                      f=1
                      return
                  else:
                      pass
          if f==0:
              try:
                  Time = [entry_D.get(),entry_M.get(),entry_Y.get()]
              except:
                  print(d,m,y)
                  Time = [d,m,y]
          for j in list(D.keys()):
              if j=='Select':
                  D.pop(j)
          if D=={}:
              tkinter.messagebox.showinfo("No input",  "Please check if you entered the items properly.")
          else:
              #print(str(D))
              #print(str(Time))
              mycursor.execute("SELECT * FROM log WHERE dates = '"+Time[2]+"-"+Time[1]+"-"+Time[0]+"'")
              if mycursor.fetchall():
                  tkinter.messagebox.showinfo("Invalid Input!",  "Data in Date already exists")
              else:
                  for i in D.keys():
                    mycursor.execute("SELECT * FROM lst WHERE Name = '" + i+"'")
                    r=mycursor.fetchall()
                    mycursor.execute("INSERT INTO log (No,Dates,Cost) VALUES (%s,%s,%s)",(int(r[0][0]),Time[2]+"-"+Time[1]+"-"+Time[0],D[i]))
                    mydb.commit()
                  tkinter.messagebox.showinfo("Updated!!",  "Congrats :)")
              
      '''def edit():
          edit=Tk()
          edit.geometry("300x130")
          edit.configure(bg='#FFFFFF')
          frame = Frame(edit,height=20,width=200,background="#00FFFF") 
          Label(frame, text="Money Manager", font=('Vladimir Script',25,'bold'),fg="#FFFFFF",bg='#00FFFF').pack()
          w = Canvas(frame,bg='#000000',height=2,highlightthickness=0,relief='ridge')
          w.pack()
          frame.pack()
          def add():
              global l
              print(l)
              LIST.append(entry_1.get())
              LIST_W.append(entry_1.get())
              if l=='501x300':
                  l="500x300"
                  root.geometry(l)
              else:
                  l="501x300"
                  root.geometry(l)
              i=len(LIST)-1
              mlabel=Label(inside_frame, text=LIST[-1],bg='#FFFFFF',font=(5))
              mlabel.grid(row=i,column=0,pady=9,padx=8,sticky='e')
              mentry=Entry(inside_frame,border=2,bg="#FFFFFF",relief='flat',highlightthickness=2,highlightcolor="#4169E1")
              entries.append(mentry)
              mentry.grid(row=i,column=1,pady=9,padx=8,sticky='e')
              return l
          def edit_destroy():
              edit.destroy()
          main_frame=Frame(edit,background="#FFFFFF")
          Expense=Label(main_frame, text="Expense Name",bg="#FFFFFF").grid(column=0,row=0,pady=10)
          entry_1=Entry(main_frame)
          entry_1.grid(column=1,row=0,pady=5,padx=10)
          main_frame.pack()
          f_b=Frame(edit,background="#FFFFFF")
          Add=Button(f_b, text="Add",font=('Ariel',8,'bold'), command= add,width=7,height=1,bg="#00FFFF",fg="#FFFFFF",activebackground="#FFFFFF",activeforeground="#00FFFF").grid(column=0,padx=5,row=0)
          Delete=Button(f_b, text="Delete",font=('Ariel',8,'bold'), command=delete,width=7,height=1,bg="#00FFFF",fg="#FFFFFF",activebackground="#FFFFFF",activeforeground="#00FFFF").grid(column=1,padx=5,row=0)
          Exit=Button(f_b, text="Exit",font=('Ariel',8,'bold'), command=edit_destroy,width=7,height=1,bg="#00FFFF",fg="#FFFFFF",activebackground="#FFFFFF",activeforeground="#00FFFF").grid(column=2,padx=5,row=0)
          f_b.pack()
          edit.mainloop()'''
      def new_add():
          global l
          global k
          option_menu.append(None)
          frame_I.append(None)
          frame_I[k] = Frame(scroll_frame,background="#FFFFFF")
          value_inside.append(None)
          value_inside[k] = tkinter.StringVar(root)
          value_inside[k].set('Select')
          c=int(str(frame_I[k])[-1])-2
          option_menu[k] = OptionMenu(frame_I[k],value_inside[k], *LIST,command = lambda LIST: disable_option(LIST,c))
          option_menu[k].config(bg="#FFFFFF")
          option_menu[k].config(fg="#000000",height=1)
          option_menu[k].config(activeforeground="#4169E1",activebackground="#FFFFFF",highlightthickness=2,relief='flat',highlightcolor="#4169E1",font=('Ariel',8,'normal'))
          option_menu[k]['menu'].config(bg="#FFFFFF",activebackground="#4169E1")
          option_menu[k].grid(row=0,column=0,pady=9,padx=8,sticky='e')
          evalue.append(None)
          evalue[k]=StringVar()
          mentry=Entry(frame_I[k],textvariable=evalue[k],border=2,bg="#FFFFFF",relief='flat',highlightthickness=2,highlightcolor="#4169E1")
          mentry.grid(row=0,column=1,pady=9,padx=8,sticky='w')
          #Delete=Button(frame_I[k],relief='flat', image=photoimage_0 , bg="#FFFFFF", name="l",command= lambda: delete(str(Delete)[-3:-2]))
          #Delete.grid(row=0,column=2,sticky='e',padx=8,pady=9)
          frame_I[k].grid(padx=95,row=k,column=0)
          k+=1
          for j in disabled.keys():
              option_menu[-1]['menu'].entryconfigure(disabled[j], state = "disable")
          if l=='401x320':
              l="400x320"
              root.geometry(l)
          else:
              l="401x320"
              root.geometry(l)
          v=True    
      entries=[]
      frame = Frame(root,height=20,width=200,background="#FFFFFF") 
      Label(frame, text="Money Manager", font=('Vladimir Script',25,'bold'),bg="#FFFFFF",fg='#00FFFF').pack(anchor='w')
      frame.pack(fill=X,padx=20,pady=5)
      '''frame = Frame(root,height=20,width=200,background="#00FFFF") 
      Label(frame, text="Money Manager", font=('Vladimir Script',25,'bold'),fg="#FFFFFF",bg='#00FFFF').pack()
      w = Canvas(frame,bg='#00FFFF',height=2,highlightthickness=0,relief='solid')
      w.pack(fill=X)
      frame.pack(fill=X)'''
      #DATE FRAME STARTS
      frame_D = Frame(root,background='#FFFFFF')
      x=datetime.datetime.now()
      global d
      global m
      global y    
      d=x.strftime('%d')
      m=x.strftime('%m')
      y=x.strftime('%y')
      def default_date():
          global Butt
          Butt = Button(frame_D, text="Show Date",relief='flat',font=('Ariel',8,'bold'), command=date,width=12,height=1,bg="#00FFFF",fg="#FFFFFF",activebackground="#FFFFFF",activeforeground="#00FFFF")
          Butt.pack(anchor='w')
          frame_D.pack(pady=7,anchor='w',fill=X,padx=45)
      def date():
          Butt.destroy()
          global entry_D
          global entry_M
          global entry_Y
          global Dater
          entry_D = Entry(frame_D,border=2,bg='#FFFFFF',width=5,relief='flat',highlightthickness=2,highlightcolor="#4169E1")
          entry_M = Entry(frame_D,border=2,bg='#FFFFFF',width=5,relief='flat',highlightthickness=2,highlightcolor="#4169E1")
          entry_Y = Entry(frame_D,border=2,bg='#FFFFFF',width=5,relief='flat',highlightthickness=2,highlightcolor="#4169E1")
          Dater = Button(frame_D, text="Hide Date",relief='flat',font=('Ariel',8,'bold'), command=destruction,width=12,height=1,bg="#00FFFF",fg="#FFFFFF",activebackground="#FFFFFF",activeforeground="#00FFFF")
          Dater.grid(row=0,column=0,padx=5,sticky='w')
          entry_D.insert(0,d)
          entry_M.insert(0,m)
          entry_Y.insert(0,y)
          entry_D.grid(row=0,column=1,padx=5)
          entry_M.grid(row=0,column=2,padx=5)
          entry_Y.grid(row=0,column=3,padx=5)          
      def destruction():
          global d
          global m
          global y     
          d=entry_D.get()
          m=entry_M.get()
          y=entry_Y.get()
          print(d,m,y)
          entry_Y.destroy()
          entry_M.destroy()
          entry_D.destroy()
          Dater.destroy()
          default_date()         
      default_date()        
      #DATE FRAME ENDS
      def Open1():
          root.destroy()
          import Settings_app
          Setting_app.settings()
      value_inside=['']
      value_inside[0] = tkinter.StringVar(root)
      main_frame = Frame(root,background="#FFFFFF",height=150)
      #Scrollbar starts
      my_canvas = Canvas(main_frame,bg="#FFFFFF",highlightthickness=0)
      my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
      my_scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
      my_scrollbar.pack(fill=Y)
      my_canvas.configure(yscrollcommand=my_scrollbar.set)
      my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
      scroll_frame = Frame(my_canvas,background="#FFFFFF")
      my_canvas.create_window((0, 0), window=scroll_frame, anchor='nw')
      frame_I=['']
      frame_I[0] = Frame(scroll_frame,background="#FFFFFF")      
      value_inside[0].set('Select')
      disabled={}
      option_menu=['']
      option_menu[0] = OptionMenu(frame_I[0],value_inside[0], *LIST,command = lambda LIST: disable_option(LIST))
      option_menu[0].config(bg="#FFFFFF")
      option_menu[0].config(fg="#000000",height=1)
      option_menu[0].config(activeforeground="#4169E1",activebackground="#FFFFFF",highlightthickness=2,relief='flat',highlightcolor="#4169E1",font=('Ariel',8,'normal'))
      option_menu[0]['menu'].config(bg="#FFFFFF",activebackground="#4169E1")
      option_menu[0].grid(row=0,column=0,pady=9,padx=8,sticky='e')
      butt_frame=Frame(scroll_frame,background="#FFFFFF")
      def disable_option(LIST,j=0):
          for i in range(len(option_menu)):
              option_menu[i]['menu'].entryconfigure(LIST, state = "disabled")
          try:
              for i in range(len(option_menu)):
                  option_menu[i]['menu'].entryconfigure(disabled[j], state = "normal")
              print(diabled[j])
          except:
              pass
          disabled[j]=LIST
          print(disabled)
      def exi():
          root.destroy()
          import Test.py
          Test.scrn()
      evalue=[None]    
      evalue[0]=StringVar()
      mentry=Entry(frame_I[0],textvariable=evalue[0],border=2,bg="#FFFFFF",relief='flat',highlightthickness=2,highlightcolor="#4169E1")
      mentry.grid(row=0,column=1,pady=9,padx=8,sticky='w')
      frame_I[0].grid(padx=95,row=0,column=0)
      butt_frame.grid(padx=95,row=1000,column=0,sticky='e')
      k=1
      photo = PhotoImage(file = "Add.png")
      photoimage = photo.subsample(20, 20)
      Ssubmit=Button(butt_frame,relief='flat',image = photoimage,bg="#FFFFFF", command=new_add)
      Ssubmit.grid(row=0,column=1,sticky='e')
      main_frame.pack(pady=7,fill=X)
      main_frame.pack_propagate(0)
      f_b= Frame(root,background="#FFFFFF")
      Submit=Button(f_b, text="Submit",font=('Ariel',8,'bold'),relief='flat', command=submit,width=7,height=1,bg="#00FFFF",fg="#FFFFFF",activebackground="#FFFFFF",activeforeground="#00FFFF").grid(column=0,padx=5,row=0)
      Exit=Button(f_b, text="Exit",font=('Ariel',8,'bold'),relief='flat', command=exi,width=7,height=1,bg="#00FFFF",fg="#FFFFFF",activebackground="#FFFFFF",activeforeground="#00FFFF").grid(column=2,padx=5,row=0)
      f_b.pack()
      Open=Button(root, text="Setting",font=('Ariel',8,'underline'),relief='flat', command=Open1,width=7,height=1,bg="#FFFFFF",fg="#4169E1").pack(pady=10)
      root.mainloop()
      on_raw = PhotoImage(file = "on.png")
      off_raw = PhotoImage(file = "off.png")
      on = on_raw.subsample(4,4)
      off= off_raw.subsample(4, 4)

  Root()

