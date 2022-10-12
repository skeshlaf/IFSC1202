x=1
y=0
z=0
a=0

while x or 0:
    x=int(input("Enter a Number (zero to quit): "))
    if x or 0:
        if z==0:
            y=x
        if x>y:
            a+=1
        z+=1
        y=x
print ("Number of Values Greater Than the Previous: ",a)