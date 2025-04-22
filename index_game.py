def access_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range."

def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value
        return f"Modified list: {lst}"
    except IndexError:
        return "Index out of range."

def slice_list(lst, start, end):
    try:
        return lst[start:end]
    except IndexError:
        return "Invalid indices."

def index_game():
    lst = [1, 2, 3, 4, 5]  # Example list
    print("🎮 Welcome to the Index Game!")
    print("📋 Current list:", lst)

    while True:
        print("\nChoose an operation:")
        print("1. Access")
        print("2. Modify")
        print("3. Slice")
        print("4. Exit")

        operation = input("Enter your choice (1/2/3/4): ")

        if operation == "1":
            index = int(input("Enter index to access: "))
            print("Result:", access_element(lst, index))

        elif operation == "2":
            index = int(input("Enter index to modify: "))
            new_value = input("Enter new value: ")
            print(modify_element(lst, index, new_value))

        elif operation == "3":
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print("Sliced portion:", slice_list(lst, start, end))

        elif operation == "4":
            print("👋 Exiting the game. Goodbye!")
            break

        else:
            print("❌ Invalid operation. Try again.")

# Run the game
index_game()
