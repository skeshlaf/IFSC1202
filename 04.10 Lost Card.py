x=int(input("Enter Number of Cards: "))
answer=0

n=x
for i in range(x-1):
  x=int(input("Enter Card: "))
  answer+=x
for i in range(n):
  n+=i
  i+=x
n-=answer
print("Missing Card: ",n)