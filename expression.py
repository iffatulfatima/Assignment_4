# **Expressions**
"""Q:1Simulate rolling two dice, three times. Prints the results of each die roll.
 This program is used to show how variable scope works."""
import random

def roll_dice():
    die1 = random.randint(1, 6)  # Local variable
    die2 = random.randint(1, 6)  # Local variable
    print(f"Dice Roll: {die1}, {die2}")

def main():
    for _ in range(3):  # Looping three times
        roll_dice()

main()

"""Q:2Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula
 (E stands for energy, m stands for mass, and C is the speed of light:
E = m * c**
Almost 100 years ago, Albert Einstein famously discovered that mass
and energy are interchangeable and are related by the above equation.
 You should ask the user for mass (m) in kilograms and use a constant value for the speed of light -- C = 299792458 m/s."""

C: int = 299792458  # The speed of light in m/s

def main():
    mass_in_kg: float = float(input("Enter kilos of mass: "))

    # Calculate energy
    # equivalently energy = mass * (C ** 2)
    # using the ** operator to raise C to the power of 2
    energy_in_joules: float = mass_in_kg * (C ** 2)

    # Display work to the user
    print("e = m * C^2...")
    print(f"e = {mass_in_kg} * {C}^2")
    C: int = 299792458  # The speed of light in m/s

def main():
    mass_in_kg: float = float(input("Enter kilos of mass: "))

    # Calculate energy
    # equivalently energy = mass * (C ** 2)
    # using the ** operator to raise C to the power of 2
    energy_in_joules: float = mass_in_kg * (C ** 2)

    # Display work to the user
    print("e = m * C^2...")
    print("m = " + str(mass_in_kg) + " kg")
    print("C = " + str(C) + " m/s")

    print(str(energy_in_joules) + " joules of energy!")

if __name__ == '__main__':
    main()


"""Q:3
Converts feet to inches. Feet is an American unit of measurement.
There are 12 inches per foot. Foot is the singular, and feet is the plural."""

INCHES_IN_FOOT: int = 12  # Conversion factor. There are 12 inches for 1 foot.

def main():
    feet: int = int(input("Enter number of feet: "))  # Get the number of feet, make sure to cast it to a float!
    inches:int = feet * INCHES_IN_FOOT  # Perform the conversion
    print("That is", inches, "inches!")


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()

"""Q:4
Write a program that asks the user for the lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!

The Pythagorean theorem, named after the ancient Greek thinker, Pythagoras, 
is a fundamental relation in geometry. It states that in a right triangle, 
the square of the hypotenuse is equal to the sum of the square of the other two sides.
For instance, let's consider a right triangle ABC, with the right angle located at C. 
According to the Pythagorean theorem:
BC ** 2 = AB ** 2 + AC ** 2
Your code should read in the lengths of the sides AB and AC, and that outputs the length of the hypotenuse (BC). You will probably find math.sqrt() to be useful.
"""
import math

# Get user input for the two perpendicular sides
AB = float(input("Enter the length of AB: "))
AC = float(input("Enter the length of AC: "))

# Calculate the hypotenuse using the Pythagorean theorem
BC = math.sqrt(AB ** 2 + AC ** 2)

# Output the result
print(f"The length of BC (the hypotenuse) is: {BC:.2f}")

"""Q:5 Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.
"""
def main():
    # Get the numbers we want to divide
    dividend: int = int(input("Please enter an integer to be divided: "))
    divisor: int = int(input("Please enter an integer to divide by: "))

    quotient: int = dividend // divisor  # Divide with no remainder/decimals (integer division)
    remainder: int = dividend % divisor  # Get the remainder of the division (modulo)

    print("The result of this division is " + str(quotient) + " with a remainder of " + str(remainder))


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()

"""Q:6 Simulate rolling two dice, and prints results of each roll as well as the total."""

import random
num_Sides:int =6

# Simulate rolling two dice
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

# Calculate total
total = dice1 + dice2

# Print results
print(f"First dice: {dice1}")
print(f"Second dice: {dice2}")
print(f"Total: {total}")

"""Q:7
Use Python to calculate the number of seconds in a year, and tell the user
what the result is in a nice print statement that looks like this (of course the value 5 should be the calculated number instead):
There are 5 seconds in a year!
You should use constants for this exercise -- there are 365 days in a year, 
24 hours in a day, 60 minutes in an hour, and 60 seconds per minute.

"""
# Define constants
Days_Per_Year: int = 365
Hours_In_a_Day: int = 24
Minutes_In_a_Hour: int = 60
Seconds_In_a_Minute: int = 60

def main():
    total_seconds = Days_Per_Year * Hours_In_a_Day * Minutes_In_a_Hour * Seconds_In_a_Minute
    print("There are " + str(total_seconds) + " seconds in a year!")


if __name__ == '__main__':
    main()

"""Q:8 Write a program which prompts the user for an adjective,
then a noun, then a verb, and then prints a fun sentence with those words!
Mad Libs is a word game where players are prompted for one word at a time, 
and the words are eventually filled into the blanks of a word template 
to make an entertaining story! We've provided you with the beginning of a sentence (the SENTENCE_START constant) which will end in a user-inputted adjective, noun, and then verb.

Here's a sample run (user input is in bold italics):
Please type an adjective and press enter. tiny
Please type a noun and press enter. plant
Please type a verb and press enter. fly
Code in Place is fun. I learned to program and used Python to make my tiny plant fly!

"""
Sentences_Start: str = "Code in Place is fun. I learned to program and used Python to make my"

def main():
  Adjective:str =input("Please Type an Adjective and Enter")
  Noun:str=input("Please Type a Noun and Enter")
  Verb:str=input("Please Type a Verb and Enter")
  print(Sentences_Start + " " + Adjective + " " + Noun + " " + Verb + "!")

if __name__ == '__main__':
    main()