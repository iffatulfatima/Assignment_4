"""Q 1: This program counts the number of times each number appears in a list. 
It uses a dictionary to keep track of the information.
An example run of the program looks like this (user input is in blue)
Enter a number: 3 Enter a number: 4 Enter a number: 3 Enter a number:
6 Enter a number: 4 Enter a number: 3 Enter a number: 12 Enter a number: 3 appears 3 times. 
4 appears 2 times. 6 appears 1 times. 12 appears 1 times."""

def get_user_numbers():
    """
    Create an empty list.
    Ask the user to input numbers and store them in a list. 
    Once they enter a blank line, break out of the loop and return the list.
    """
    user_numbers = []
    while True:
        user_input = input("Enter a number: ")
        
        # If the user enters a blank line, break out of the loop and stop asking for input
        if user_input == "":
            break
        
        # convert the user input to an integer and add it to the list
        num = int(user_input)
        user_numbers.append(num)
    
    return user_numbers

def count_nums(num_lst):
    """
    Create an empty dictionary.
    Loop over the list of numbers. 
    If the number is not in the dictionary, add it as a key with a value of 1.
    If the number is in the dictionary, increment its value by 1.
    """
    num_dict = {}
    for num in num_lst:
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
    
    return num_dict


def print_counts(num_dict):
    """
    Loop over the dictionary and print out each key and its value.
    """
    for num in num_dict:
        print(str(num) + " appears " + str(num_dict[num]) + " times.")


def main():
    """
    Ask the user to input numbers and store them in a list. Once they enter a blank line,
    print out the number of times each number appeared in the list.
    """
    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)


# Python boilerplate.
if __name__ == '__main__':
    main()

    """Q:2 In this program we show an example of using dictionaries to keep track of information in a phonebook."""


def read_phone_numbers():
    
    # Ask the user for names/numbers to story in a phonebook (dictionary).
        # Returns the phonebook
    phonebook = {}                   # Create empty phonebook

    while True:
        name = input("Name: ")
        if name == "":
            break
        number = input("Number: ")
        phonebook[name] = number

    return phonebook


def print_phonebook(phonebook):
    """
    Prints out all the names/numbers in the phonebook.
    """
    for name in phonebook:
        print(str(name) + " -> " + str(phonebook[name]))


def lookup_numbers(phonebook):
    """
    Allow the user to lookup phone numbers in the phonebook
    by looking up the number associated with a name.
    """
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name not in phonebook:
            print(name + " is not in the phonebook")
        else:
            print(phonebook[name])


def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)


# Python boilerplate.
if __name__ == '__main__':
    main()

    """Q:3 There's a small fruit shop nearby your house that you like to buy from. 
Since you buy several fruit at a time, you want to keep track of how much the fruit will cost before you go.
Luckily you wrote down what fruits were available and how much one of each fruit costs.
Write a program that loops through a dictionary of fruits,
prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.
Here is an example run of the program (user input is in bold italics):
How many (apple) do you want?: 2
How many (durian) do you want?: 0
How many (jackfruit) do you want?: 1
How many (kiwi) do you want?: 0
How many (rambutan) do you want?: 1
How many (mango) do you want?: 3
Your total is $99.5"""

def main():
    fruits = {'apple': 1.5,
             'durian': 50,
            'jackfruit': 80,
            'kiwi':2,
            'rambutan': 11,
            'mango': 5}
    
    total_cost = 0
    for fruit_name in fruits:
        price = fruits[fruit_name]
        amount_bought = int(input("How many (" + fruit_name + ") do you want to buy?: "))
        total_cost += (price * amount_bought)
    
    print("Your total is $" + str(total_cost))


if __name__ == '__main__':
    main()



    """ Q: 4 You want to be safe online and use different passwords for different websites.
However, you are forgetful at times and want to make a program that can match which password 
belongs to which website without storing the actual password!
This can be done via something called hashing. Hashing is when we take something and
convert it into a different, unique identifier. This is done using a hash function. Luckily,
there are several resources that can help us with this.
For example, using a hash function called SHA256(...) something as simple as
hello
can be hashed into a much more complex
2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
Fill out the login(...) function for a website that hashes their passwords.
Login should return True if an email's stored password hash in stored_logins is the same as the 
hash of password_to_check.
(Hint. You will need to use the provided hash_password(...) function.
You don't necessarily need to know how it works, just know that hash_password(...) returns the hash 
for the password!)"""
import hashlib

def hash_password(password):
    """
    Hashes the password using SHA256 and returns the hex digest.
    """
    return hashlib.sha256(password.encode()).hexdigest()

def login(email, password_to_check, stored_logins):
    """
    Checks if the hashed password_to_check matches the stored hash
    for the given email in stored_logins.
    
    Returns True if it matches, False otherwise.
    """
    if email not in stored_logins:
        return False
    
    hashed_input_password = hash_password(password_to_check)
    return hashed_input_password == stored_logins[email]

# Example usage:
# Suppose you registered with these passwords
stored_logins = {
    "user1@example.com": hash_password("mySecret123"),
    "user2@example.com": hash_password("helloWorld"),
    "user3@example.com": hash_password("pass1234")
}

# Testing login attempts
print(login("user1@example.com", "mySecret123", stored_logins))  # True
print(login("user2@example.com", "wrongPass", stored_logins))     # False
print(login("user4@example.com", "pass1234", stored_logins))      # False (email doesn't exist)
