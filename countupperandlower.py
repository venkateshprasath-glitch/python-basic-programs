txt=input("enter a string: ")
uppercase=0
lowercase=0
for ch in txt:
    if ch.isupper():
        uppercase +=1
    else:
        lowercase +=1
print("uppercase letters:",uppercase)
print("lowercase letters:",lowercase)
