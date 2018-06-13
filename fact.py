n=int(input())
fact=1
if n<0:
	print('factorial does not exist')
elif n==0:
	print('factorial of zero is 0')
else:
	for i in range(1,n+1):
		fact=fact*i
	print(fact)
