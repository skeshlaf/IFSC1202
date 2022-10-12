z = int(input("Enter N: "))
count = 0

for i in range(z):
    if int(input("Enter Number: ")) == 0:
        count += 1
print('Number of Zeros:',(count))