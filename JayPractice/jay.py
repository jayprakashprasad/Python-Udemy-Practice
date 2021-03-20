# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
from fractions import Fraction
import datetime
person = dict(name='hello',Age=21)
print(id(person))
print(person['name'])

person['name']= 'hell'
print(person['name'])
print(id(person))
print(person['name'])


person['married']='no'
print(person['married'])
print(type('married'))

hgell= "jje"
print(hgell)
print(id(hgell))
print(id(person))

u =10%6
print(u)
pr =10//89
print(pr)

xi=0b111 
yi=0b101 
print(xi & yi)
print(xi | yi)


x= True and True and False
y=True and False  and True

print((x+y))

x = 10 
print(x)
xFloat = str(x)
print(xFloat)
print(type(xFloat))
print(x)

for i in range(6,13): 
   print(i, end ="  ") 
print() 

Dib=("what ur name")
print(Dib)
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

x = 5
y = 10

def SwapNumber(x,y):
   x = 5
   y = 10
   # Add code to swap numbers x,y here


x, y = y, x
print("x =", x)
print("y =", y)
return[x,y]

#while
i = 0
while i < 6:
  i += 1
  if i == 0:
    continue #also break
  print(i)

i = 0
while i < 6:
  i += 1
  if i == 4:
    break
  print(i)


#loop
l=[1,2,3,"w3",round(4.55)]
for i in l:
  print(i) #simplest way
  
l=[1,2,3,"w3"]
for inn in range(4):
  print("indexc[{}]={}".format(inn,l[inn]))

l=[1,2,3,"w3",round(4.55)]
for i in l:
  print(l)
  break #its important
  
l=[1,2,3,"w3"]
for inn in range(6):
  print(l[2])



 #file reading
  f = open("demtoTxt.txt","r" )
  f= openf = open("D:\\myfiles\welcome.txt", "r") #if the file is in different folder
  print(f.read())
   #or print(f.readLine()) #reads a separate line
   #"r","w","x","a"
  
# or in loop
def main():
   try: 
     f= open("demotxt.txt","r")
     for x in f:
       print(x)
     f.close()
   except IOError:
      print("file not found")
   print("app is done")
if __name__ == '__main__':main()



























