
#from ____ import MultiOperations //if we import  to from another page
 
class Operations:
    def sum(self,n1,n2):
        return  n1+n2
    def div(self,n1,n2):
        return n1/n2

class MultiOperations(Operations):
    def mul(self,n1,n2):
        return n1*n2
    def sum(self,n1,n2):

        return  (n1+n2)*2

def main():
    muOp=MultiOperations()
    print("mul={}".format(muOp.mul(1,3)))
    print("mul={}".format(muOp.div(1,3)))



if __name__ == '__main__':main()




