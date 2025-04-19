"""Write a simple joke bot. The bot starts by asking the user what they want. However,
 your program will only respond to one response: Joke.
If the user enters Joke then we will print out a single joke. Each time the joke is always the same:
Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store.
A programmer tells her: get a liter of milk, and if they have eggs, get 12. 
Sophia returns with 13 liters of milk.
The programmer asks why and Sophia replies: 'because they had eggs'
If the user enters anything else we print out:
Sorry I only tell jokes
You should use the three constants:
PROMPT JOKE SORRY
which contain the strings for the prompt asked to the user,
the joke to print out if the user enters Joke and the sorry message if the user enters anything else.
Your program will need to use an if statement which checks if the user input is Joke:
if user_input == "Joke":
Recall that == is a comparison which tests if two values are equal to one another.
Here is a full run of the program (user input is in blue):
What do you want? Joke Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store.
A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'

"""
# Define constants
PROMPT = "What do you want? "
JOKE = ("Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store. "
        "A programmer tells her: get a liter of milk, and if they have eggs, get 12. "
        "Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'")
SORRY = "Sorry I only tell jokes"

# Ask user for input
user_input = input(PROMPT)

# Respond based on input
if user_input == "Joke":
    print(JOKE)
else:
    print(SORRY)

"""Write a program that asks a user to enter a number. Your program will then double that number 
and print out the result. It will repeat that process until the value is 100 or greater.
For example if the user enters the number 2 you would then print:
4 8 16 32 64 128
Note that:
2 doubled is 4
4 doubled is 8
8 doubled is 16
and so on.
We stop at 128 because that value is greater than 100.
Maintain the current number in a variable named curr_value. When you double the number, you should be updating curr_value.
Recall that you can double the value of curr_value using a line like:
curr_value = curr_value * 2
This program should have a while loop and the while loop condition should test
if curr_value is less than 100. Thus, your program will have the line:
while curr_value < 100:"""

# Ask the user for a number
curr_value = int(input("Enter a number: "))

# Double the number repeatedly and print each value until it's 100 or more
while curr_value < 100:
    curr_value = curr_value * 2
    print(curr_value)

"""Write a program that prints out the calls for a spaceship that is about to launch.
Countdown from 10 to 1 and then output Liftoff!
Here's a sample run of the program:
10 9 8 7 6 5 4 3 2 1 Liftoff!
There are many ways to solve this problem. One approach is to use a for loop, and to use the for loop variable
i. Recall that i will keep track of how many times the for loop has completed executing its body.
As an example this code:
for i in range(10): print(i)
Will print out the values 0, 1, 2, 3, 4, 5, 6, 7, 8, 9. The values printed in liftoff are 10 minus the
number of times the for loop has completed.
"""
# Countdown from 10 to 1
for i in range(10):
    print(10 - i, end=' ')

# Print Liftoff at the end
print("Liftoff!")

# Guess My Number

"""I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high
Enter a new number: 25 Your guess is too low
Enter a new number: 40 Your guess is too low
Enter a new number: 45 Your guess is too low
Enter a new number: 48 Congrats! The number was: 48"""

import random

# Generate a random number between 0 and 99
secret_number = random.randint(0, 99)

print("I am thinking of a number between 0 and 99...")

# Ask the user to make a guess
guess = int(input("Enter a guess: "))

# Loop until the user guesses correctly
while guess != secret_number:
    if guess > secret_number:
        print("Your guess is too high")
    else:
        print("Your guess is too low")
    # Ask for a new guess
    guess = int(input("Enter a new number: "))

# Correct guess
print(f"Congrats! The number was: {secret_number}")


"""Print 10 random numbers in the range 1 to 100.
Here is an example run:
45 79 61 47 52 10 16 83 19 12
Each time you run your program you should get different numbers
81 76 70 1 27 63 96 100 32 92
Recall that the python random library has a function randint which returns an integer in the range set by the parameters (inclusive). For example
this call would produce a random integer between 1 and 6, which could include 1 and could include 6:
value = random.randint(1, 6)"""

import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    """
    Generates and prints N_NUMBERS random integers between MIN_VALUE and MAX_VALUE.
    """
    for _ in range(N_NUMBERS):
        number = random.randint(MIN_VALUE, MAX_VALUE)
        print(number, end=' ')
    print()  # for a newline at the end

if __name__ == '__main__':
    main()
