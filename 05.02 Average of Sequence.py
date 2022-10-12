x=0
y=0

while True:
    num=int(input("Enter a Number (zero to quit): "))
    if num==0:
        break
    x+=num
    y+=1
if y==0:  
    print ("Sequence Length is 0")
else:
    print ("Average: ",x/y)