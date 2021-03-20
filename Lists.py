
ages=[22,3,44,50,99,1] #  mutable # can change
print(ages)
print("append element")
ages.append(100)
print(ages)
print("insert in specific place")
ages.insert(1,55)
print(ages)

print("words split")
str="welcome into python3 project"
words=str.split(' ')
print(words)
print(words[0:3])


##########
from functools import reduce
li=[10,2,3,4,8,11]
def highest_even(li):
  evens = []
  for item in li:
    if item % 2 == 0:
      evens.append(item)
  return (evens)
print(min(highest_even(li)))

hgell= ""

print(id(hgell))

listi= [1,2,3,4,5,6,7,8,9]

sum1=reduce(lambda x,y:x+y,listi)
print(sum1)

print ("The maximum element of the list is : ",end="") 
print (reduce(lambda a,b : a if a == b else b,listi)) 