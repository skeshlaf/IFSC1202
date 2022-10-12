import random
print("Winners and Losers - Human is Even, Computer is Odd")

human=0
computer=0

for i in range(5):
    print('Round: {}'.format(i+1))
    humannum=int(input("Enter your Guess: "))
    computernum=random.randint(1,5) #(Hint: use randint)
    
    if (humannum+computernum)%2==0:
        human=human+1
        
    else:
        computer=computer+1
    print('Human Guess: {} - Computer Guess: {}'.format(humannum,computernum))

    if (humannum+computernum)%2==0:
        print("Sum is even.")
    else:
        print("Sum is odd.")

    print("Human Score: {} - Computer Score: {}".format(human,computer))

if human>computer:
        print("\nHuman Wins!")
else:
        print("\nComputer Wins!")
        

