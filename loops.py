"""Q 1: Guess My Number
I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high
Enter a new number: 25 Your guess is too low
Enter a new number: 40 Your guess is too low
Enter a new number: 45 Your guess is too low
Enter a new number: 48 Congrats! The number was: 48"""


import random

def main():
    # Generate the secret number at random!
    secret_number = random.randint(1, 99)
    
    print("I am thinking of a number between 1 and 99...")
    
    # Get user's guess
    guess = int(input("Enter a guess: "))
    # True if guess is not equal to secret number
    while guess != secret_number:
        if guess < secret_number:  # If-statement is True if guess is less than secret number
            print("Your guess is too low")
        else:
            print("Your guess is too high")
            
        guess = int(input("Enter a new guess: "))  # Get a new guess from the user
        
    print("Congrats! The number was: " + str(secret_number))
    
if __name__ == '__main__':
    main()

"""Q:2 Write a program to print terms in the Fibonacci sequence up to a maximum value.
In the 13th century, the Italian mathematician Leonardo Fibonacci,
as a way to explain the geometric growth of a population of rabbits, 
devised a mathematical sequence that now bears his name. The first two terms in this sequence,
 Fib(0) and Fib(1), are 0 and 1, and every subsequent term is the sum of the preceding two. Thus, the first several terms in the Fibonacci sequence look like this:
Fib(0) = 0 Fib(1) = 1 Fib(2) = 1 = 0 + 1 Fib(3) = 2 = 1 + 1 Fib(4) = 3 = 1 + 2 Fib(5) = 5 = 2 + 3
Write a program that displays the terms in the Fibonacci sequence, 
starting with Fib(0) and continuing as long as the terms are less than 10,000
(you should store this value as a constant!). Thus, your program should produce the following sample run:
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765
"""
MAX_TERM_VALUE : int = 10000

def main():
    curr_term = 0  # The 0th Fibonacci Number
    next_term = 1  # The 1st Fibonacci Number
    while curr_term <= MAX_TERM_VALUE:
        print(curr_term)
        term_after_next = curr_term + next_term
        curr_term = next_term
        next_term = term_after_next


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()

"""Q:3 Write a program that prints the first 20 even numbers. There are several correct approaches, 
but they all use a loop of some sort. Do no write twenty print statements
The first even number is 0:
0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38
"""
def even_number():
    # This for-loop start at 0 and counts up to 19 (for a total of 20 numbers)
    for i in range(20):
        print(i * 2)  # Use the 'i' value inside the for-loop
   
# Call the main function when "run", no need to edit anything below!
if __name__ == "__main__":
    even_number()


"""Q:4 Write a program which prompts the user to type an affirmation of your choice
(we'll use "I am capable of doing anything I put my mind to.") until they type it correctly.
Sometimes, especially in the midst of such uncertain times, we just need to be reminded
that we are resilient, capable, and strong; this little Python program may be able to help!
Here's a sample run of the program (user input is in blue):
Please type the following affirmation: I am capable of doing anything I put my mind to.
Hmmm That was not the affirmation. Please type the following affirmation: 
I am capable of doing anything I put my mind to. I am capable of doing anything I put my mind to. That's right! :)
Note that you can call input() with no prompt and it will still wait for a user to type something!"""

AFFIRMATION : str = "I am capable of doing anything I put my mind to."

def main():
    print("Please type the following affirmation: " + AFFIRMATION)

    user_feedback = input()  # Get user's input
    while user_feedback != AFFIRMATION:  # While the user's input isn't the affirmation
        # Tell the user that they did not type the affirmation correctly
        print("That was not the affirmation.")

        # Ask the user to type the affirmation again!
        print("Please type the following affirmation: " + AFFIRMATION)
        user_feedback = input()

    print("That's right! :)")

if __name__ == '__main__':
    main()


""" Q:5 Write a program that prints out the calls for a spaceship that is about to launch.
Countdown from 10 to 1 and then output Liftoff!
Here's a sample run of the program:
10 9 8 7 6 5 4 3 2 1 Liftoff!
There are many ways to solve this problem. One approach is to use a for loop, and to use the for loop variable i. Recall that i will keep track of 
how many times the for loop has completed executing its body. As an example this code:
for i in range(10): print(i)
Will print out the values 0, 1, 2, 3, 4, 5, 6, 7, 8, 9. 
The values printed in liftoff are 10 minus the number of times the for loop has completed.
"""
for i in range(10, 0, -1):
    print(i, end=" ")

print("Liftoff!")


"""Write a program that asks a user to enter a number. 
Your program will then double that number and print out the result.
 It will repeat that process until the value is 100 or greater.
For example if the user enters the number 2 you would then print:
4 8 16 32 64 128
Note that:
2 doubled is 4
4 doubled is 8
8 doubled is 16
and so on.
We stop at 128 because that value is greater than 100.
Maintain the current number in a variable named curr_value.
When you double the number, you should be updating curr_value.
Recall that you can double the value of curr_value using a line like:
curr_value = curr_value * 2
This program should have a while loop and the while loop condition should test if curr_value is less than 100.
Thus, your program will have the line:
while curr_value < 100:"""

# Ask the user to enter a number
curr_value = int(input("Enter a number: "))

# Loop until curr_value is 100 or greater
while curr_value < 100:
    curr_value = curr_value * 2
    print(curr_value, end=" ")
