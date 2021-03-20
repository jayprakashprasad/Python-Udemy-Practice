
def main():
  f=open("demtoTxt.txt","r" )
  f.write("hello")
  f.close()

#another method
  def main():
      f=open("demotxt.txt","a")
      for i in range(5)
        inputs=input("please write your name")
        f.write("\n {}".format(inputs))
      f.close()

#read file
def main():
 
  f=open("demtoTxt.txt","r" )
    for line in f:
        print(line)
    f.close()
 

  if __name__ == '__main__':main()


 
#######
def read():
    f=open("text.txt","w" )
    f.write("hello")
    f.close()


def Display():
     print("hello")
     
def sum(n1,n2):
    z =n1+n2
    return z

def main():
    Display()
    Results=sum(10,10)
    print(Results)
  # Results=sum(11,12)
  #print("sum","=",Results)


#######
def Display():
     print("hello")
     
def sum(n1,n2):
    z =n1+n2
    return z

x=10 #Global var
def Show():
     global x
     print(x)

def mains():
    global x
    print("x={}".format(x))
    Show()    

def mainss():
    Display()
    print(sum(10,10))
    mains()
    read()
    
if __name__ == '__main__':mainss()