x=0
y=0
z=0
while True:
    number=int(input("Enter a Number (zero to quit): "))
    if(number==0): break 
    y+=1
    if number>x:
        x,z=number,y
print("Maximum: {}".format(x))
print("Index of Maximum: {}".format(z))