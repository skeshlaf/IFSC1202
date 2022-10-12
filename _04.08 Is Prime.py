def if_prime(N):
    for i in range (2,N):
        if (N % i)==0:
            return False
        else:
            return True 
N=int(input("Enter N: "))
if if_prime(N):
    print("PRIME")
else: 
    print("COMPOSITE")



