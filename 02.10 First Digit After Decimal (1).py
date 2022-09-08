import math
x= float(input("Enter Number: "))
fractional, whole = math.modf(x)
y= (fractional%10)*10
print ("Tenths Value ", math.floor(y))