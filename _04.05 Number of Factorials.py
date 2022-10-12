n=int(input("Enter N: "))

sum =0

for i in range (1,n+1):
    partialfactorial =1
    for j in range (1,i+1):
        partialfactorial=partialfactorial*j
    sum=sum+partialfactorial
    
print ('Sum of Factorials: ',partialfactorial)