max=0
while True:
    x=int(input("Enter a Number (zero to quit): "))
    if x>max:
        count=1
        max=x
    elif x==max:
        count+=1
    elif x==0:
        break 

print ("Maximum: ",max)
print ("Number of Occurrences: ",count)
