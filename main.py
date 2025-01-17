from art import logo
import random

def guesschecker(n,g,a):
    if n==g:
        print(f"You got it! The answer was {g}")
    else:
        a-=1
        if n>g:
            print("Too low")
        if n<g:
            print("T0o high")
        if a!=0:
         print("Guess again.")
    return a


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number=random.randint(1,100)
print(number)
difficulty=input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty=="easy":
    attempts=10
else:
    attempts=5

guess=0
while attempts>0 and guess is not number:
    print(f"You have {attempts} attempts")
    guess=int(input("Make a guess: "))
    attempts=guesschecker(number,guess,attempts)
    if attempts==0:
        print("You've run out of guesses. Run again")

