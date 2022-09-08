x = int(input("Enter a 3 Digit Number: "))
y=0

while x != 0

z = x % 10                  
y = y * 10 + z 
z //= 10                      
print("Reversed number: ", (y))