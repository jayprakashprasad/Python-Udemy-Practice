
##watch the constructor method
class Car:
    def SetType(self,type):
        self.Type=type
    def GetType(self):
        return self.Type
    def SetModel(self,model):
        self.Model=model
    def GetModel(self):
        return self.Model
    def SetPrice(self,price):
        self.Price=price
    def GetPrice(self):
        return self.Price
    def SetMilesDrive(self,milesDrive):
        self.MilesDrive=milesDrive
    def GetMilesDrive(self):
        return self.MilesDrive
    def SetOwner(self,owner):
        self.Owner=owner
    def GetOwner(self):
        return self.Owner
    def GetCurrentPrice(self):
        return self.GetPrice()- ( self.GetMilesDrive()*10)



def main():
    myCar= Car()
    myCar.SetType("BMW")
    myCar.SetModel(2015)
    myCar.SetPrice(26000)
    myCar.SetMilesDrive(15)
    myCar.SetOwner("Hussein")
    CurrentPrice=myCar.GetCurrentPrice()
    print("{}'s Car, New price {}".format(myCar.GetOwner(),CurrentPrice))


    AlexCar= Car()
    AlexCar.SetType("GMC")
    AlexCar.SetModel(2017)
    AlexCar.SetPrice(28000)
    AlexCar.SetMilesDrive(5)
    AlexCar.SetOwner("Alex")
    CurrentPrice=AlexCar.GetCurrentPrice()
    print("{} 's Car, New price {}".format(AlexCar.GetOwner(),CurrentPrice))




if __name__ == '__main__':main()
