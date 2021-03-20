
from tkinter import *
from tkinter import ttk
root=Tk()
button=ttk.Button(root,text="click me")
button.pack()
def BuClick():
    print("Butyton cis clicked")

button.config(command=BuClick)

button.invoke()

button.state(["disabled"])

button.state(['!disabled'])

button.instate(['!disabled'])

#####2
from tkinter import *
from tkinter import ttk
root=Tk()

entry=ttk.Entry(root,width=50)
entry.pack()
button=ttk.Button(root,text="click me")
button.pack()

def BuClick():
    print(entry.get())
    #entry.delete(0,END)
    #entry.insert(0,"ckcccccc")
   

button.config(command=BuClick)
  
root.mainloop()

#3
from tkinter import *
from tkinter import ttk
  
def BuClick(id):
    print("id:{}".format(id))

root=Tk()
ttk.Button(root,text="click me", command=lambda :BuClick(10)).pack()

root.mainloop()

#4
from tkinter import *
from tkinter import ttk
  
root=Tk()

def BuClick(event):
    print("id:{}".format(event.type))
def ButtOn(event):
    print("clicked")

def BtoNn(event):
  print("hru")

bu=ttk.Button(root,text="click me")
bu.pack()
bu.bind("<ButtonPress>",ButtOn)

bk=ttk.Button(root,text="clikc her")
bk.pack()
bk.bind("<Button-1>",BtoNn)

root.bind("<Control-v>",BuClick)


root.mainloop()

#5
from tkinter import *
from tkinter import ttk

root=Tk()
button1=ttk.Button(root,text="click me")
button1.pack()
button2=ttk.Button(root,text="click me2")
button2.pack()
button3=ttk.Button(root,text="click me3")
button3.pack()

style=ttk.Style()
style.theme_names()
style.theme_use()
style.theme_use("classic")
style.configure('TButton',foreground='red')
button3.winfo_class()

style.configure('TButton',foreground='red',font=('Arial',24))
style.configure('Info.TButton',foreground='blue',font=('Arial',18,'bold'))

button3.configure(style='Info.TButton')
style.map('Info.TButton',background=[('pressed','blue'),('disabled','grey')])
button3.state(['disabled'])

##2.2
from tkinter import *
from tkinter import ttk

root=Tk()
style=ttk.Style()
style.configure('TButton',background='red',font=('Arial',24))
entry=ttk.Entry(root,width=50)
entry.pack()
button=ttk.Button(root,text="click me")
button.pack()
logo=PhotoImage(file="")
button.config(image=logo,compound=LEFT)
Resize_Logo=logo.submap(10,10)
button.config(image=Resize_Logo)

def BuClick():
    print(entry.get())
    #entry.delete(0,END)
    #entry.insert(0,"ckcccccc")
   

button.config(command=BuClick)
  
root.mainloop()


#6
from tkinter import *
from tkinter import ttk

root=Tk()
style=ttk.Style()
style.theme_use("classic")

ttk.Label(root,text'Green',background='Green').grid(row=0,column=0,padx=5,pady=5,sticky='snew')
ttk.labelLabel(root,text'Blue',background='blue').grid(row=0,column=1,ipadx=5,ipady=5,sticky='snew')
ttk.Label(root,text'Yellow',background='blue').grid(row=0,column=2,rowspan='2',sticky='snew')
ttk.Label(root,text'Orange',background='orange').grid(row=1,column=0,columnspan='2',sticky='snew')

root.rowconfigure(0,weight=2)
root.rowconfigure(1,weight=1)

root.columnconfigure(1,weight=1)
root.columnconfigure(2,weight=2)



root.mainloop()

#7
from tkinter import *
from tkinter import ttk

root=Tk()

frame1=ttk.Frame(root)
frame1.pack()
frame1.config(height=200,width=200,relief=RIDGE,padding=(10,10))
ttk.Button(frame1,text="clicke").grid(row=0,column=0)
ttk.Button(frame1,text="clicke").grid(row=0,column=3)

frame2=ttk.Frame(root)
frame2.pack()
frame2.config(height=200,width=200,relief=RIDGE,padding=(10,10))
ttk.Button(frame2,text="clicke").pack()
ttk.Button(frame2,text="clicke").pack()

ttk.LabelFrame(frame1,text="clicke",height=100,width=100).pack()



root.mainloop()

#8
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root.title("login page")
root=Tk()
root.resizable(True,True)
#root.resizable(False,False)


l1=ttk.Label(text="username")
l1.grid(row=0,column=0)

etUserName=ttk.Entry(root,width=20)
etUserName.grid(row=0,column=1)

l2=ttk.Label(text="password")
l2.grid(row=1,column=0)

etPassword=ttk.Entry(root,width=20)
etPassword.grid(row=1,column=1)
etPassword.config(show'*')

Bulogin=ttk.Button(root,text="login")
Bulogin.grid(row=2,column=1)

def BuClick():
    print("username{},passwrods{}".format(etUserName.get(),etPassword.get()))
    
    if(etUserName.get()=="jay" and etPassword.get()=="1234" )
      messagebox.showinfo(title="login info",message="username{},passwrods{}".format(etUserName.get(),etPassword.get())
    else:
      messagebox.showinfo(title="login info",message="wrong info")


Bulogin.config(command=BuClick)

root.mainloop()


#9
from tkinter import *
from tkinter import ttk

root=Tk()

cb=ttk.Checkbutton(root,text='is married')
cb.pack()

state=StringVar()
state.set('yes')
state.get()

cb.config(variable=state,onvalue='yes married',offvalue='no isnot')
state.get()

rbVar=StringVar()
rb1=ttk.Radiobutton(root,text='male',variable=rbVar,value="is male")
rb1.pack()
rbVar.get()

rb2=ttk.Radiobutton(root,text='female',variable=rbVar,value="is female")
rb2.pack()

rb3=ttk.Radiobutton(root,text='female2',variable=rbVar,value="is not female")
rb3.pack()

rbVar.get() #when click on check and radio button

#10
from tkinter import *
from tkinter import ttk

root=Tk()
tv=ttk.Treeview()
tv.pack()
tv.insert('','0','item1',text='jay')
tv.insert('','0','item2',text='j')
tv.insert('','0','item3',text='ja')

tv.move('item2','item1','0')
tv.move('item3','item1,'end')
tv.insert('item1','0','item4',text='rnaa')

tv.item('item1',open=True)

tv.detach('item4')
tv.move('item4','','end')
tv.delete('item4')

tv.configure(column=('age'))

tv.column('age',width=60,anchor='center')

tv.column('#0',width=80,anchor='center')
tv.column('#0',width=100,anchor='center')

tv.heading('#0',text='name')
tv.heading('age',text='age')

tv.set('item1','age','28')
tv.set('item2','age','2')
tv.set('item3','age','1')

def tvSelect(event):
    print(tv.selection())
tv.bind('<<TreeviewSelect>>',tvSelect)








