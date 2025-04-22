"""Now practice writing code with lists! Implement the functionality described in the comments below.

def main(): # Create a list called fruit_list that contains the following fruits: # 'apple', 'banana', 'orange', 'grape', 'pineapple'.

"""
def main():
    fruit_list = ["apple", "banana", "orange", "grapes", "pineapple"]
    
    # Print the length of the list.
    print("Length of the list:", len(fruit_list))

    # Add 'mango' at the end of the list. 
    fruit_list.append("mango")

    # Print the updated list.
    print("Updated list:", fruit_list)


if __name__ == "__main__":
    main()
