a=input()
str=""
for i in range (0,len(a),2):
    str=str+a[i+1]
    str=str+a[i]
str.strip()
print(str)
