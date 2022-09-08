import math
x= int(input("Enter a Number: "))
y=[(x//(10**i))%10 for i in range(math.ceil(math.log(x,10))-1]
print('Ones Digit: ',y)
z= (round(x/10))
print('Tens Digit: ',z)