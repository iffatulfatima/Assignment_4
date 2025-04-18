""" Q:1 Write a program that prints the first 20 even numbers. 
There are several correct approaches, but they all use a loop of some sort.
Do no write twenty print statements
The first even number is 0:
0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38

"""
def print_even_numbers():
    for i in range(20):
        print(i * 2, end=' ') # end = ' ' ensures all numbers are printed on the same line, separated by spaces.

print_even_numbers()



""" Q:2 Write a program which asks a user for their age and lets them know if they can or can't vote in the following three fictional countries.

Around the world, different countries have different voting ages. In the fictional countries of Peturksbouipo, Stanlau, and Mayengua, the voting ages are very different:

the voting age in Peturksbouipo is 16 (in real life, this is the voting age in, for example, Scotland, Ethiopia, and Austria)

the voting age in Stanlau is 25 (in real life this is the voting age in the United Arab Emirates)

the voting age in Mayengua is 48 (in real life, as far as we can tell, this isn't the voting age anywhere)

Your code should prompt the for their age and print whether or not they can vote in Peturksbouipo, Stanlau, or Mayengua.

Here's a sample run of the program (user input is in blue):

How old are you? 20 You can vote in Peturksbouipo where the voting age is 16. You cannot vote in Stanlau where the voting age is 25. You cannot vote in Mayengua where the voting age is 48.

"""


def check_voting_eligibility():
    age = int(input("How old are you? "))

    if age >= 16:
        print("You can vote in Peturksbouipo where the voting age is 16.")
    else:
        print("You cannot vote in Peturksbouipo where the voting age is 16.")

    if age >= 25:
        print("You can vote in Stanlau where the voting age is 25.")
    else:
        print("You cannot vote in Stanlau where the voting age is 25.")

    if age >= 48:
        print("You can vote in Mayengua where the voting age is 48.")
    else:
        print("You cannot vote in Mayengua where the voting age is 48.")

check_voting_eligibility()


""" Q:3 Write a program that reads a year from the user and tells whether a given year is a leap year or not.

A leap year (also known as an intercalary year or bissextile year) is a calendar year that contains an additional day (or, in the case of a lunisolar calendar, a month) added to keep the calendar year synchronized with the astronomical year or seasonal year. In the Gregorian calendar, each leap year has 366 days instead of 365, by extending February to 29 days rather than the common 28.

In the Gregorian calendar, three criteria must be checked to identify leap years:

The given year must be evenly divisible by 4;
If the year can also be evenly divided by 100, it is NOT a leap year; unless:
The year is also evenly divisible by 400. Then it is a leap year.
Your code should use the above criteria to check for a leap year and then print either 
"That's a leap year!" or "That's not a leap year."
"""
year = int(input("Enter a year: "))

# Check for leap year using the Gregorian calendar rules
if (year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print("That's a leap year!")
        else:
            print("That's not a leap year.")
    else:
        print("That's a leap year!")
else:
    print("That's not a leap year.")


""" Q: 4 Write a program which asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height.

In amusement parks (ah, the good old pre-pandemic days...), rollercoasters frequently have minimum height requirements for safety reasons. Assume for now that the minimum height is 50 of whatever height unit you'd like

Here's two sample runs (user input is in bold italics):

How tall are you? 100

You're tall enough to ride!

How tall are you? 10

You're not tall enough to ride, but maybe next year!

(For an extra challenge, write code which will repeatedly ask a user how tall they are and tell them whether or not they're tall enough to ride, until the user doesn't enter a height at all, in which case the program stops. Curious about how to do this? See the function tall_enough_extension() in the solution code!)

"""
# Set the minimum height required
MIN_HEIGHT = 50

# Ask the user for their height
height_input = input("How tall are you? ")

# Convert the input to an integer
height = int(height_input)

# Check if the user is tall enough
if height >= MIN_HEIGHT:
    print("You're tall enough to ride!")
else:
    print("You're not tall enough to ride, but maybe next year!")


""" Q:5 Print 10 random numbers in the range 1 to 100.
Here is an example run:
45 79 61 47 52 10 16 83 19 12
Each time you run your program you should get different numbers
81 76 70 1 27 63 96 100 32 92
Recall that the python random library has a function randint which returns an integer in the range set by the parameters (inclusive). For example this call would produce a random integer between 1 and 6,
which could include 1 and could include 6:
value = random.randint(1, 6)
"""

import random

# Generate and print 10 random numbers between 1 and 100
for _ in range(10):
    value = random.randint(1, 100)
    print(value, end=' ')
