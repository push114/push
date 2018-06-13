
n=int(input())
reverse=0
while (n>0):
    Reminder = n %10
    reverse = (reverse *10) + Reminder
    n= n //10
    print(reverse)
