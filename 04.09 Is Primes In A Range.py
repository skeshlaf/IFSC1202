def if_prime(N):
     for i in range (2,N):
        if (N%i)==0:
            return False 
     else: 
        return True

A=int(input("Enter A: "))
B=int(input("Enter B: "))
for N in range(A,B+1):
    if if_prime(N):
        if if_prime(N):
            print(N)
        