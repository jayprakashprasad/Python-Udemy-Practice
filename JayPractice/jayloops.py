 #######
  # Write Python 3 code in this online editor and run it.

l=[1,2,3,"w3",round(4.55)]
for i in l:
  print(i)

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

i=0
while(i<5):
    j=0
    while(j<5):
        print("(i,j)=({},{})".format(i,j))
        j+=1
        i+=1
    
word="Python"
for  letter in word:
    if(letter=='t'):
        continue;
    print(letter)




def main():
  l =[1,33,45,32,55,22,23,100]
  for item in l:
    if(item==55):
        print("number is found {}".format(item))
        break;

    
if __name__ == '__main__':main()