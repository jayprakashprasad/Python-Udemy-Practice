from tkinter import *
from tkinter import ttk

root=Tk()
tv=ttk.Treeview()
tv.pack()
tv.insert('','0','item1',text='jay')
tv.insert('','0','item2',text='j')
tv.insert('','0','item3',text='ja')

tv.move('item2','item1','0')
tv.move('item3','item1','end')
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
