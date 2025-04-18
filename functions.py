"""Write a function that takes two numbers and finds the average between the two."""
# def average(a: int, b: int):

#     # Returns the number which is half way between a and b
    
#     sum = a + b
#     return sum / 2

# def main():
#     avg_1 = average(0, 5)
#     avg_2 = average(8, 16)
    
#     final = average(avg_1, avg_2)
#     print("avg_1", avg_1)
#     print("avg_2", avg_2)
#     print("final", final)


# if __name__ == '__main__':
#     main()

"""Fill out the chaotic_counting() function, which prints the numbers from 1 to 10, but with a catch.
We've written a done() function which returns True with likelihood DONE_LIKELIHOOD -- 
at each number, before printing the number, you should call done() and check if it returns True or not. 
If done() returns True, we're done counting, and you should use a return statement to end the chaotic_counting() function execution and resume execution of main(), which will print "I'm done.". We've written main() for you -- check it out! Notice that we'll only print "I'm done" from main() once chaotic_counting() is done with its execution.
Here's a sample run of this program:
I'm going to count until 10 or until I feel like stopping, whichever comes first. 1 2 3 I'm done.
"""

# import random

# DONE_LIKELIHOOD = 0.5  # Adjust this value if needed

# def done():
#     return random.random() < DONE_LIKELIHOOD

# def chaotic_counting():
#     for i in range(1, 11):  # Counting from 1 to 10
#         if done():
#             return  # Exit the function if done() returns True
#         print(i, end=" ")

# def main():
#     print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
#     chaotic_counting()
#     print("\nI'm done.")

# # Run the program
# main()

"""Fill out the function count_even(lst) which
first populates a list by prompting the user for integers until 
they press enter (please use the prompt "Enter an integer or press enter to stop: "),
and then prints the number of even numbers in the list.
If you'd prefer to focus on the second task only, scroll down for our implementation of the first task!

"""


def count_even(lst):
    """
    Returns number of even numbers in list.
    >>> count_even([1,2,3,4])
    2
    >>> count_even([1,3,5,7])
    0
    """
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    return count  # ✅ Return instead of print


def get_list_of_ints():
    """
    Reads in integers until the user presses enter and returns the resulting list.
    """
    lst = []
    user_input = input("Enter an integer or press enter to stop: ")
    while user_input != "":
        try:
            lst.append(int(user_input))
        except ValueError:
            print("Invalid input. Please enter an integer.")
        user_input = input("Enter an integer or press enter to stop: ")
    return lst


def main():
    lst = get_list_of_ints()
    even_count = count_even(lst)
    print(f"Number of even numbers: {even_count}")  # ✅ Now print from here


if __name__ == '__main__':
    main()


"""Fill out the double(num) function to return the result of multiplying num by 2.
We've written a main() function for you which asks the user for a number,
calls your code for double(num) , and prints the result.
Here's a sample run of the program (user input in bold italics):
Enter a number: 2 Double that is 4
"""

def double(num):
    return num * 2

def main():
    user_input = input("Enter a number: ")
    number = int(user_input)
    result = double(number)
    print(f"Double that is {result}")

if __name__ == '__main__':
    main()


"""Fill out the get_name() function to return your name as a string!
 We've written a main() function for you which calls your function to
retrieve your name and then prints it in a greeting.
Here's a sample run of the program where the name we've
decided to return is Sophia (the autograder expects the returned name to be Sophia):
Howdy Sophia ! 🤠
"""

def get_name():
    return "Anam"

def main():
    name = get_name()
    print(f"Noman {name} ! 🤠")

if __name__ == '__main__':
    main()
"""10 even 11 odd 12 even 13 odd 14 even 15 odd 16 even 17 odd 18 even 19 odd"""

def main():
    for i in range(10):
        if is_odd(i):
            print('odd')
        else:
            print('even')
            
def is_odd(value: int):
    """
    Checks to see if a value is odd. If it is, returns true.
    """
    
    remainder = value % 2  # 0 if value is divisible by 2, 1 if it isn't
    return remainder == 1

if __name__ == '__main__':
    main()
    

"""Write the helper function print_divisors(num), 
which takes in a number and prints all of its divisors 
(all the numbers from 1 to num inclusive that num can be cleanly divided by 
(there is no remainder to the division). Don't forget to call your function in main()!
Here's a sample run (user input is in blue):
Enter a number: 12 Here are the divisors of 12 1 2 3 4 6 12
"""

def print_divisors(num: int):
    print("Here are the divisors of", num)
    for i in range(num):
        current_divisor = i + 1
        if num % current_divisor == 0:
            print(current_divisor)

def main():
    num = int(input("Enter a number: "))
    print_divisors(num)


if __name__ == '__main__':
    main()

"""Fill out print_multiple(message, repeats), which takes as parameters a string message to print,
 and an integer repeats number of times to print message. 
 We've written the main() function for you, which prompts the user for a message and a number of repeats.
Here's a sample run of the program (user input is in blue):
Please type a message: Hello! Enter a number of times to repeat your message: 
6 Hello! Hello! Hello! Hello! Hello! Hello!
"""

def print_multiple(message, repeats):
    for _ in range(repeats):
        print(message, end=' ')

def main():
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    print_multiple(message, repeats)

if __name__ == '__main__':
    main()
"""Implement the helper function make_sentence(word, part_of_speech) which will take a string word
and an integer part_of_speech as parameters and, depending on the part of speech,
place the word into one of three sentence templates (or one from your imagination!):
If part_of_speech is 0, we will assume the word is a noun and use the template:
"I am excited to add this ____ to my vast collection of them!"
If part_of_speech is 1, we will assume the word is a verb use the template:
"It's so nice outside today it makes me want to ____!"
If part_of_speech is 2, we will assume the word is an adjective and use the template:
"Looking out my window, the sky is big and ____!" make_sentence(word, part_of_speech) 
should not return anything, just print the correct sentence with the word filled in the blank.
Here's a sample run of the program (user input is in blue):
Please type a noun, verb, or adjective: groovy Is this a noun, verb, or adjective?
Type 0 for noun, 1 for verb, 2 for adjective: 2 Looking out my window, the sky is big and groovy!"""

def make_sentence(word, part_of_speech):
    if part_of_speech == 0:
        print(f"I am excited to add this {word} to my vast collection of them!")
    elif part_of_speech == 1:
        print(f"It's so nice outside today it makes me want to {word}!")
    elif part_of_speech == 2:
        print(f"Looking out my window, the sky is big and {word}!")
    else:
        print("Invalid part of speech. Please enter 0, 1, or 2.")

def main():
    word = input("Please type a noun, verb, or adjective: ")
    part = int(input("Is this a noun, verb, or adjective? Type 0 for noun, 1 for verb, 2 for adjective: "))
    make_sentence(word, part)

if __name__ == '__main__':
    main()

"""Write a function called print_ones_digit , which takes as a parameter an integer num
and prints its ones digit. The modulo (remainder) operator, %, should be helpful to you here.
Call your function from main()!
Here's a sample run (user input is in blue):
Enter a number: 42 The ones digit is 2
"""

def print_ones_digit(num):
    ones_digit = num % 10  # Get the ones digit using the modulo operator
    print(f"The ones digit is {ones_digit}")

def main():
    user_input = input("Enter a number: ")
    number = int(user_input)
    print_ones_digit(number)

if __name__ == '__main__':
    main()
