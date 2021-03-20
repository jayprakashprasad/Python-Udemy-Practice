
#correct method  #1
class Car:
    def __init__(self,type,model,price,milesDrive,owner):
        self.Type=type
        self.Model=model
        self.Price=price
        self.MilesDrive=milesDrive
        self.owner=owner

    def GetType(self):
        return self.Type
    def GetModel(self):
        return self.Model
    def GetPrice(self):
        return self.Price
    def GetMilesDrive(self):
        return self.MilesDrive
    def GetOwner(self):
        return self.owner

    def GetCurrentPrice(self):
        return self.GetPrice()- ( self.GetMilesDrive()*10)
    
    def myFunc(self):
        print("iam:{}".format(self.owner))


p1=Car("bmw",2015,20000,14,"jay")
print(5-5)
print(p1.Type)
print(p1.Model)

print(p1.Price)
print(p1.MilesDrive)
print(p1.owner)
print("my name is :{}--{}".format(p1.owner,p1.Price))
print("price:{}--".format(p1.GetPrice()-p1.GetMilesDrive()))
print("price:{}--".format(p1.Price-p1.MilesDrive*10 ))
p1.myFunc()












#return self.GetPrice()- ( self.GetMilesDrive()*10)








#2

class Cars:
    def __init__(self,type,model,price,milesDrive,owner):
        self._Type=type
        self._Model=model
        self._Price=price
        self._MilesDrive=milesDrive
        self._Owner=owner

    def GetType(self):
        return self._Type
    def GetModel(self):
        return self._Model
    def GetPrice(self):
        return self._Price
    def GetMilesDrive(self):
        return self._MilesDrive
    def GetOwner(self):
        return self._Owner

    def GetCurrentPrice(self):
        return self.GetPrice()- ( self.GetMilesDrive()*10)



def main():
    myCar= Car("BMW",2015,26000,15,"Hussein")
    CurrentPrice=myCar.GetCurrentPrice()
    print("{}'s Car, New price {}".format(myCar.GetOwner(),CurrentPrice))


    AlexCar= Car("GMC",2017,28000,5,"Alex")
    CurrentPrice=AlexCar.GetCurrentPrice()
    print("{} 's Car, New price {}".format(AlexCar.GetOwner(),CurrentPrice))




if __name__ == '__main__':main()


