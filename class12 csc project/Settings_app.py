from tkinter import *
import tkinter.messagebox
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sql12345",
  database="project"
)
mycursor = mydb.cursor()
def settings():
    def goback():
        roots.destroy()
        import Updator
        Updator.up()
    def ini():
      print("///")  
      mycursor.execute("SELECT * FROM lst")
      r=mycursor.fetchall()
      LIST=[]
      for i in r:
        LIST.append(i[1])
      return LIST  

    global Item
    global is_on
    global LIST
    global Type
    LIST=ini()
    roots = Tk()
    roots.title('Item update')
    roots.geometry("500x300")
    roots.configure(bg="white")
    frame = Frame(roots,height=20,width=200,background="#FFFFFF") 
    Label(frame, text="Money Manager", font=('Vladimir Script',25,'bold'),bg="#FFFFFF",fg='#00FFFF').pack(anchor='w')
    frame.pack(fill=X,padx=20,pady=5)
    is_on = True
    def add():
        global Item
        global is_on
        global LIST
        global Type
        It=Item.get()
        mycursor.execute("SELECT Live FROM lst WHERE Name='"+str(It)+"'")
        r=mycursor.fetchall()
        if It in LIST :
            if r[0][0]:
                tkinter.messagebox.showinfo("Invalid Input!",  "Item already exists")
            else:
                mycursor.execute("UPDATE lst SET Live=1 WHERE Name='"+str(It)+"'")
                mydb.commit()
        else:
            mycursor.execute("INSERT lst (No, Name,Live) VALUES (%s,%s,%s)",(len(LIST)+1,It,1))
            mydb.commit()
        LIST=ini() 
    def dele():
        global Item
        global is_on
        global LIST
        It=Item.get()
        mycursor.execute("SELECT Live FROM lst WHERE Name='"+str(It)+"'")
        r=mycursor.fetchall()
        if (It in LIST) and r:  
            mycursor.execute("UPDATE lst SET Live=NULL WHERE Name='"+str(It)+"'")
            mydb.commit()
            LIST=ini()
        else:
            tkinter.messagebox.showinfo("Invalid Input!",  "Please enter an existing Item")
##    def switch():
##        global is_on
##        if is_on:
##            on_button.config(bg = "#FF0000", text="Expense")
##            is_on = False
##        else:
##            on_button.config(bg = "#00FF00",text="Income")
##            is_on = True        
    ram=Frame(roots,background="#FFFFFF")
    lbl3=Label(ram,bg="#FFFFFF", text="Enter the item you want to add/delete")
    Item=Entry(ram,width=20, font=('calibre',10,'normal'),relief='flat',highlightthickness=2,highlightcolor="#4169E1")        
    lbl3.grid(row=0,column=0,padx=25,sticky='w')
    Item.grid(row=0,column=1,padx=2,sticky='w')
##    on_button = Button(ram,bg='#00FF00',text="Income", bd = 0,highlightthickness=0,command = switch,width=7,height=1,relief='flat',font=('Ariel',12,'normal'))
##    on_button.grid(row=1,column=0,padx=25,pady=20,sticky='w')
    add_button = Button(ram,text="Add",bg="#7CFC00",fg="#FFFFFF", bd = 0,highlightthickness=0,width=7,height=1,relief='flat',font=('Ariel',12,'normal'),command=add)
    back_button = Button(ram,text="Go back",bg="#7CFC00",fg="#FFFFFF", bd = 0,highlightthickness=0,width=7,height=1,relief='flat',font=('Ariel',12,'normal'),command=goback)
    add_button.grid(row=2,column=0,padx=25,pady=20,sticky='w')
    back_button.grid(row=3,column=0,padx=25,pady=20,sticky='w')
    del_button = Button(ram,text="Delete",bg="#EE4B2B",fg="#FFFFFF", bd = 0,highlightthickness=0,width=7,height=1,relief='flat',font=('Ariel',12,'normal'),command=dele)
    del_button.grid(row=2,column=1,padx=25,pady=20,sticky='e')

    ram.pack(pady=20)

    roots.mainloop()
settings()

        
