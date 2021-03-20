from tkinter import *
from  tkinter import ttk
from  tkinter import messagebox
from  DbConnectClass import DBConnect

dbconnect=DBConnect()

root= Tk()

ttk.Label(root,text="Full Name").grid(row=0,column=0)
EntryFullName=ttk.Entry(root ,width=30,font=('Arial,10'))
EntryFullName.grid(row=0,column=1,columnspan=2)

root.configure(background='#e1d8b2')
style=ttk.Style()
style.theme_use('classic')
style.configure('TLable',background='blue')
style.configure('TButton',background='blue',foreground="white")
style.configure('TRadiobutton',background='blue',foreground="white")




SpanGender=StringVar()
SpanGender.set('Male')
ttk.Label(root,text="Gender").grid(row=1,column=0)

ttk.Radiobutton(root,text="male",variable=SpanGender,value="Male").grid(row=1,column=1)
ttk.Radiobutton(root,text="Female",variable=SpanGender,value="Female").grid(row=1,column=2)

TextComments=Text(root,width=20,height=15,font=('Arial',16))
TextComments.grid(row=3,column=1,columnspan=2)

ttk.Label(root,text="Comments").grid(row=3,column=0)
buButton=ttk.Button(root,text="Submit")
buButton.grid(row=4,column=3)

def ButtonClick():
    print("fullname:".format(EntryFullName/get()))
    print("gender:".format(SpanGender.get()))
    print("comments:".format(TextComments.get(1.0,'end')))

    msg=dbConnect.Add(EntryFullName.get(),spanGender.get(),TextComments.get(1.0,'end'))
    messagebox.showinfo(title='Add info',message=sg)
    EntryFullName.delete(10.'end')
    TextComments.delete(1.0,'end')

buButton.comfig(command=ButtonClick())






root.mainloop()