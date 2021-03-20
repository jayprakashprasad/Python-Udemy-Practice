import datetime

def main():
    #main code function
    DOB=input("Enter your DOB:")
    CurrentYear=datetime.datetime.now().year
    Age=CurrentYear-int(DOB)
    print("Your age is {}".format(Age))


#having two methods
def main():
    Display()
    Results=sum(10,10)
    print(Results)
  # Results=sum(11,12)
    print("sum","=",Results)

#######
def Display():
     print("hello")
     
def sum(n1,n2):
    z =n1+n2
    print(z)

def main():
    Display()
    sum(10,10)
   
    


if __name__ == '__main__':main()
