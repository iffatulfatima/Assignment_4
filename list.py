"""Q:1 Write a function that takes a list of numbers and returns the sum of those numbers."""
def sum_of_numbers():
  sum_of_numbers:int = [20,4,6,8,10]
  print(sum(sum_of_numbers))


if __name__ == '__main__':
    sum_of_numbers()

"""Q:2 Write a program that doubles each element in a list of numbers. For example, if you start with this list:
numbers = [1, 2, 3, 4]
You should end with this list:
numbers = [2, 4, 6, 8]"""

def double_each_elements():
  numbers:list[int] =[2,3,4,5,6]
  for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
  print(numbers)

if __name__ == '__main__':
    double_each_elements()

"""Q:3 Implement an 'eraser' on a canvas.

The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen.
 We then create an eraser rectangle which, when dragged around the canvas,
 sets all of the rectangles it is in contact with to white."""

import tkinter as tk

# Grid and eraser config
CELL_SIZE = 40
ROWS = 10
COLS = 10
ERASER_SIZE = 60

class CanvasEraserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Canvas Eraser")

        self.canvas = tk.Canvas(root, width=COLS*CELL_SIZE, height=ROWS*CELL_SIZE, bg="white")
        self.canvas.pack()

        self.cells = []
        self.create_grid()

        # Initial eraser position
        self.eraser = self.canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, outline="gray", fill="gray", stipple="gray25")
        
        self.dragging = False
        self.canvas.bind("<ButtonPress-1>", self.start_drag)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drag)

    def create_grid(self):
        for row in range(ROWS):
            row_cells = []
            for col in range(COLS):
                x1 = col * CELL_SIZE
                y1 = row * CELL_SIZE
                x2 = x1 + CELL_SIZE
                y2 = y1 + CELL_SIZE
                rect = self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="black")
                row_cells.append(rect)
            self.cells.append(row_cells)

    def start_drag(self, event):
        self.dragging = True
        self.move_eraser(event)

    def stop_drag(self, event):
        self.dragging = False

    def on_drag(self, event):
        if self.dragging:
            self.move_eraser(event)

    def move_eraser(self, event):
        x = event.x - ERASER_SIZE // 2
        y = event.y - ERASER_SIZE // 2
        self.canvas.coords(self.eraser, x, y, x + ERASER_SIZE, y + ERASER_SIZE)
        self.erase_cells()

    def erase_cells(self):
        ex1, ey1, ex2, ey2 = self.canvas.coords(self.eraser)
        for row in self.cells:
            for cell in row:
                cx1, cy1, cx2, cy2 = self.canvas.coords(cell)
                if self.is_overlap(ex1, ey1, ex2, ey2, cx1, cy1, cx2, cy2):
                    self.canvas.itemconfig(cell, fill="white")

    def is_overlap(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        return not (ax2 < bx1 or ax1 > bx2 or ay2 < by1 or ay1 > by2)

if __name__ == "__main__":
    root = tk.Tk()
    app = CanvasEraserApp(root)
    root.mainloop()
"""Q:4 In the information flow lesson, we discussed using a variable storing a number as an example
 of scope. We saw that changes we made to the number inside a function did not stay unless we returned it. This is true for what we call immutable data types which include things like numbers and strings.

However, there are also mutable data types where changes stay even if we don't return anything.
Some examples of mutable data types are lists and dictionaries. This means that you should be mindful when modifying lists and dictionaries within helper functions since their changes stay whether or not you return them.

To see this in action, fill out the add_three_copies(...) function which takes a list and some data and then adds three copies of the data to the list.

 Don't return anything and see what happens! Compare this process to the x = change(x) example and note the differences.

Here is an example run of this program (user input in bold italics):

Enter a message to copy: Hello world!

List before: []

List after: ['Hello world!', 'Hello world!', 'Hello world!']

(Note. The concept of immutable/mutable data types is called mutability. Be careful because different programming languages have different rules regarding mutability!)"""


def add_three_copies(my_list,data):
  for i in range(3):
    my_list.append(data)
def main():
  message:str=input("Enter a message to copy")
  my_list=[]
  print("List_before:",my_list)
  add_three_copies(my_list,message)
  print("List_after:",my_list)
if __name__ == '__main__':
  main()

"""Q:5 Fill out the function get_first_element(lst) which takes in a list lst as a parameter and prints the first element in the list. The list is guaranteed to be non-empty. We've written some code 
for you which prompts the user to input the list one element at a time."""

def get_first_element(first):
    """
    Prints the first element of a provided list.
    """

    print(first[0])

def get_first():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    first = []
    element: str = input("Please enter an element of the list or press enter to stop. ")
    while element != "":
        first.append(element)
        element = input("Please enter an element of the list or press enter to stop. ")
    return first

def main():
    first = get_first()
    get_first_element(first)


if __name__ == '__main__':
    main()

"""Q:6 Fill out the function get_last_element(lst) which takes in a list lst as a parameter
 and prints the last element in the list. The list is guaranteed to be non-empty, 
 but there are no guarantees on its length.

"""
def get_last_element(lst):
    """Prints the last element of the provided list."""
    print(lst[-1])  # Access and print the last element using negative indexing

def main():
    n = int(input("Enter the number of elements in the list: "))  # Get the list size
    user_list = []

    for i in range(n):
        element = input(f"Enter element {i + 1}: ")  # Get each element
        user_list.append(element)

    get_last_element(user_list)  # Call the function to print the last element

# Required to call the main function
if __name__ == '__main__':
    main()
"""Q:7 Write a program which continuously asks the user to enter values which are added one by one into a list. 
When the user presses enter without typing anything, print the list.
Here's a sample run (user input is in blue):
Enter a value: 1 Enter a value: 2 Enter a value: 3 Enter a value: Here's the list: ['1', '2', '3']"""

def main():
    list = []  # Make an empty list to store things in

    value = input("Enter a value: ")  # Get an initial value
    while value:  # While the user input isn't an empty value
        list.append(value) # Add value to list
        value = input("Enter a value: ")  # Get the next value to add

    print("Here's the list:", list)



if __name__ == '__main__':
    main()

"""Q:7 Fill out the function shorten(lst) which removes elements from the end of lst,
 which is a list, and prints each item it removes until lst is MAX_LENGTH items long.
If lst is already shorter than MAX_LENGTH you should leave it unchanged.
We've written a main() function for you which gets a list and passes it into your function once you run the program. For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program.

"""
MAX_LENGTH = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        removed = lst.pop()  # Remove from end
        print(removed)

def main():
    # Example list - you can change it to test
    sample_list = [10, 20, 30, 40, 50]
    shorten(sample_list)
    print("Final list:", sample_list)

if __name__ == "__main__":
    main()
