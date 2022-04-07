import random
# n will be the number that the computer chooses for you to guess.
n = random.randint(1, 99)

# guess is the number that you put in.
guess = int(input("Enter an integer from 1 to 99: "))

#conditionals. while the computers number does not equal your guess run this loop. 
while n != "guess":
    if guess < n:
        print("guess is low")
        guess = int(input("Enter an integer from 1 to 99: "))
    elif guess > n:
        print("guess is high")
        guess = int(input("Enter an integer from 1 to 99: "))
    else:
        print("you guessed it!")
        break
    