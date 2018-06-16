
a=[]
n=int(input("enter the number opf elements in the array"))
for i in range(1,n+1):
    b=(input())
    a.append(b)
  
a.sort(key=len)
print (a)
