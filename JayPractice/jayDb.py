
import sqlite3 
db=sqlite3.connect("information.db")



def createTable():
     db.row_factor=sqlite3.Row
     db.execute("create table if not exists Admin(ID integer primary key autoincrement, name text,age int)")
     db.commit()


def Add(name,age):
    db.row_factor=sqlite3.Row
    #add records
    db.execute("insert into admin(name,age)values(?,?)",(name,age))
    db.commit()
    print("added successfully")
 
def ListAdmins():
    cursor=db.execute("select * from admin")
    for row in cursor:
         print("ID:{}, name:{},age:{}".format(row["ID"],row["name"],row["age"]))

def DeleteRecord(ID):
    db.row_factor=sqlite3.Row
    #add records
    db.execute("delete from admin where ID='{}'".format(ID))
    db.commit()
    print("deleted successfully")

def UpdateRecord(ID,age):
    db.row_factor=sqlite3.Row
    #add records
    db.execute("update admin set=? where ID=?",(age,ID))
    db.commit()
    print("updated successfully")

def main():
    createTable()
    while 1:
        IndexOp=int(input("\n==\nSelect Operation,"
                            "1- Add\n"
                            "2- ListAdmin:\n3- delete\n 4- update age\n 0- exit\n==\n Index number"))
        if(IndexOp==0)
            break:
        elif(IndexOp==1):
                name=input("Enter name")
                Age=int(input("enter age:"))
                Add(name,age)
        elif(IndexOp==2):
                ListAdmins()

        elif(IndexOp==3):
            ID=int(input("enter your ID"))
            Deleterecord(ID) 

        elif(IndexOp==4):
                ID=int(input("Enter person id"))
                Age=int(input("enter new age:"))
                UpdateRecord(ID,age)

if __name__ == '__main__':main()

# def main() sample eg to create table
 #   db=sqlite3.connect("information.db")
 #   db.row_factor=sqlite3.Row
#    db.execute("create table if not exists Admin(name text,age int)")
  #  db.commit() 
  #https://www.python.org/downloads

