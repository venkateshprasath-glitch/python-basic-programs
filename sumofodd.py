num=int(input("enter a number:"))
total=0
for n in range(1,num+1):
    if n%2!=0:
        total+=n
print("sum of odd numbers:",total)