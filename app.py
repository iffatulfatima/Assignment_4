""" Write a Python program that takes two integer inputs from the user and calculates their sum.
 The program should perform the following tasks:
Prompt the user to enter the first number.
Read the input and convert it to an integer.
Prompt the user to enter the second number.
Read the input and convert it to an integer.
Calculate the sum of the two numbers.
 Print the total sum with an appropriate message."""

def main():
    # Prompt the user to enter two integers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Calculate the sum
    total = num1 + num2

    # Print the result
    print(f"The sum of {num1} and {num2} is {total}.")

# Run the program
if __name__ == "__main__":
    main()

"""Q:2 Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).

What's your favorite animal? cow

My favorite animal is also cow!

"""
def main():
    # Ask the user for their favorite animal
    favorite_animal = input("What's your favorite animal? ")

    # Respond with a message including the user's input
    print(f"My favorite animal is also {favorite_animal}!")

# Run the program
if __name__ == "__main__":
    main()
"""Q:3 Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.

The Celsius scale is widely used to measure temperature, but places still use Fahrenheit. Fahrenheit is another unit for temperature, but the scale is different from Celsius -- for example, 0 degrees Celsius is 32 degrees Fahrenheit!

The equation you should use for converting from Fahrenheit to Celsius is the following:

degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0

(Note. The .0 after the 5 and 9 matters in the line above!!!)

"""
def main():
    # Prompt the user to enter temperature in Fahrenheit
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    # Convert Fahrenheit to Celsius
    celsius = (fahrenheit - 32) * 5.0 / 9.0

    # Display the result
    print(f"Temperature: {fahrenheit}F = {celsius}C")

# Run the program
if __name__ == "__main__":
    main()
"""Q:4 Write a program to solve this age-related riddle!

Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

Anton is 21 years old.
Beth is 6 years older than Anton.
Chen is 20 years older than Beth.
Drew is as old as Chen's age plus Anton's age.
Ethan is the same age as Chen.
Your code should store each person's age to a variable and print their names and ages at the end. The autograder is sensitive to capitalization and punctuation, be careful! Your solution should look like this (the below numbers are made up -- your solution should have the correct values!):
Anton is 3
Beth is 4
Chen is 5
Drew is 6
Ethan is 7
"""
def main():
    # Storing each friend's age in variables based on the clues provided
    anton_age = 21
    beth_age = anton_age + 6  # Beth is 6 years older than Anton
    chen_age = beth_age + 20  # Chen is 20 years older than Beth
    drew_age = chen_age + anton_age  # Drew's age is Chen's age plus Anton's age
    ethan_age = chen_age  # Ethan is the same age as Chen

    # Printing the names and ages
    print(f"Anton is {anton_age}")
    print(f"Beth is {beth_age}")
    print(f"Chen is {chen_age}")
    print(f"Drew is {drew_age}")
    print(f"Ethan is {ethan_age}")

# Run the program
if __name__ == "__main__":
    main()

"""Q:5 Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).

Here's a sample run of the program (user input is in bold italics):
What is the length of side 1? 3
What is the length of side 2? 4
What is the length of side 3? 5.5
The perimeter of the triangle is 12.5

"""
def main():
    # Prompt the user to enter the lengths of the sides
    side1 = int(input("What is the length of side 1? "))
    side2 = int(input("What is the length of side 2? "))
    side3 = int(input("What is the length of side 3? "))

    # Calculate the perimeter
    perimeter = side1 + side2 + side3

    # Print the perimeter
    print(f"The perimeter of the triangle is {perimeter}")

# Run the program
if __name__ == "__main__":
    main()
"""Q:6Ask the user for a number and print its square (the product of the number times itself).
Here's a sample run of the program (user input is in bold italics):
Type a number to see its square: 4
4.0 squared is 16.0

"""
def main():
    # Ask the user to input a number
    number = float(input("Type a number to see its square: "))

    # Calculate the square of the number
    square = number ** 2


    # Print the result
    print(f"{number} squared is {square}")

# Run the program
if __name__ == "__main__":
    main()
