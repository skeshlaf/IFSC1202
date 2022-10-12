x=0
while True:
    number=int(input("Enter a Number (zero to quit):"))
    if number ==0: break
    if number %2==0:x+=1
print ("Number of Even Numbers: ",x)