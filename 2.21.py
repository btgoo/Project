# # Question 1
#
# # Define the dictionary
# function_dict = {}
#
# # Define the functions
# def multiply_by_2(x):
#     return x * 2
#
# def square(x):
#     return x ** 2
#
# # Store function names as keys and functions themselves as values
# function_dict[multiply_by_2] = 'Multiply by 2'
# function_dict[square] = 'Power of 2'
#
# # Call functions using the dictionary
# print(function_dict[multiply_by_2])
# print(function_dict[square])

# Question 2

# Define the function
def find_indices(table, target):

    # If there is nothing on table, return None
    if not table:
        return None

    # Define a list
    targets = []
    # Iterate enumerated table
    for i, row in enumerate(table):
        # Create nested loop in order to iterate the row we found
        for j, value in enumerate(row):
            # In the iterated row, if there is a value that matches our target, we append indices to our list
            if value == target:
                targets.append((i, j))
    return targets

plants = [
    ["apple", "banana", "orange"],
    ["potato", "carrot", "onion"],
    ["cactus", "rose", "lavender"]
]

element = "apple" # Any type of element, in this example, I chose string
indices = find_indices(plants, element)
if indices:
    print(f"Element {element} found at indices:")
    # For loop to print everytime that appended in the list.
    for index in indices:
        print(index)

# Question 3

# Define the function
# def function():
#     # A while loop to keep the code repeating
#     while True:
#         # Use 'try' so that the code will not crash and prints message
#         try:
#             x_input = input("Enter the x value (or type 'quit' to exit): ")  # Prompt user to enter the x
#             if x_input.lower() == 'quit':
#                 break  # Exit the loop if input is 'quit'
#             x = int(x_input)
#             value = x ** 2 + 3 * x - 5  # Calculate the value
#             print(f"The value of given number is {value}")  # Print the value
#
#         # If any value error happens such as giving string as input or leaving blank, it prints a message
#         except ValueError:
#             print("Please enter a numerical value")
#
#
# function()

# Question 4

# Look at the code below and answer the following questions:
# i)	What data structure do you expect the input to be? - Dictionary
# ii)	On which line is the product_data first accessed by the function? - Line 3
# iii)	On which line is string formatting used? - Line 4 because we are converting int to str
# iv)	What is the type of the total_sales? - Either int or float
# v)	Add appropriate comments to the code below.

# Define function
# def process_product_sales(product_data):  # Line 1
#     # Line 2
#     # Get names from the file
#     product_name = product_data["name"]  # Line 3
#     # Get sales from the file
#     product_sales = product_data["sales"]  # Line 4
#     # Line 5
#     # Calculate the total sales by summing up product sales
#     total_sales = sum(product_sales)  # Line 6
#     # Average sales is defined by diving total sales by the number of data points
#     average_sales = total_sales / len(product_sales)  # Line 7
#     # Store product name and its average sales in a list
#     product_info = [product_name, average_sales]  # Line 8
#     # Line 9
#     # Output the result with string formatting
#     return f"Product: {product_info[0]}, Average Sales: {product_info[1]}" # Line 10

# Question 5
#
# class Students:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades
#
# class Gradebook:
#     def __init__(self, students):
#
#
#     def calculate_average_grade(students):
#         """
#        Calculate the average grade for a list of students.
#
#        Args:
#        - students (list of dicts): List of student dictionaries containing "name" and "grades" keys
#
#        Returns:
#        - float: Average grade for all students
#        """
#         total_grade = sum(sum(student["grades"]) for student in students)
#         total_students = sum(len(student["grades"]) for student in students)
#         return total_grade / total_students
#
#
# This code is intended to calculate the area of a rectangle.

def calculate_area(rectangle_length, rectangle_width):
    area = rectangle_length * rectangle_width  # rectangle_height -> rectangle_width
    return area


length = 3
width = 3

rectangle_area = calculate_area(length, width)

print("Area of the rectangle:", rectangle_area)