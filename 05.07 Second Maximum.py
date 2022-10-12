highest=0
index =0
highest_index =0

x=int(input("Enter First Number: "))
y=int(input("Enter Second Number: "))

while True:
    num = int(input('Enter a Number ( zero to quit): '))
    if(num==0): break
    index+=1
    if num>highest:
        highest,highest_index=num,index


print('First Maximum: {}'.format(highest))
print('Second Maximum: {}'.format(highest_index))