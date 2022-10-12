number=int(input("Enter N: "))

if (number<=9):
    for x in range(1,number+1):
        for y in range(1,x+1):
            print(y,end='')
        print()
                 
