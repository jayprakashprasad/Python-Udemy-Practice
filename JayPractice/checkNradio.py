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