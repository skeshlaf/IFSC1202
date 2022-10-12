count=0
Sum=0
minimum=0
maximum=0

while 1:
    n = float(input("Enter a Value (zero to quit):"))   
    if n ==0:
        print("Count:     ",count)
        print("Sum:       ",Sum)
        if count==0:
            print("Average:   ","Not defined")
        else:
            print("Average:   ",Sum/count)
        print("Minimum:   ",minimum)
        print("Maximum:   ",maximum)
        break
    else:
        count +=1
        Sum +=n
        
       
        if count ==1:
            maximum = n
            minimum = n
        
       
        if n > maximum:
            maximum = n
        if n < minimum:
            minimum = n