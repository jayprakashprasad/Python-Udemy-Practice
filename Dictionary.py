person=dict(Name="hussein",Age=27,Salary=80000) # mutable
print(person)
print(person["Name"])
print("update name")
person["Name"]="Hussein Alrubaye"
print(person["Name"])
print("add Insurance key")
person["Insurance"]="Yes"
print(person)
print("delete age")
del person["Age"]
print(person)
#print Salary
print(person["Salary"])

##differ
thisdict =	{ "brand": "Ford","model": "Mustang","year": 1964}
print(thisdict)

##nested dict
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
for x,y in myfamily.items():
  print(x,y)

  
###

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
    print(x)
    
thisdicts =	{"brand":"Ford","year":1964,"model":"Mustang"}
print(thisdicts)
for xi,y in thisdicts.items():
    print(xi,y)
thisdicts.popitem()
print(thisdicts)

jay = { "name":"jayy"}
jay1 = { "age":1 }
myxx = { 
    "jay":jay,
    "jay1":jay1
}    
print(myxx)

jay = dict(name="jayy")
jay1 = dict(age=1 )
myxx = dict( 
    jay=jay,
    jay1=jay1
)
print(myxx)
myxx.pop('jay')
print(myxx)

##
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
for x,y in myfamily.items():
  print(x,y)
