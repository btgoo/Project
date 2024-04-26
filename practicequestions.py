# # # Question 1
#
# M = [["Baxter", "Bingo", "Balius"],
#     ["Rover", "Ruffles", "Ran"],
#     ["Kane", "Kibbles", "Kratos"]]
#
# def printthird():
#     for lists in M:
#         for names in lists:
#             if names == lists[2]:
#                 print(names)
#
# printthird()

# # Question 2
#
# def sqrt():
#     number = float(input("number:"))
#     guess = float(input("guess:"))
#     n = 1
#     while n <= 1000:
#         guess = 1/2 * (guess + number/guess)
#         n += 1
#     print(guess)
#
# sqrt()

# Question 3

# a=2
# b=5
# c=20
# x = not((a - 7) > b) and (2*b + a < c)
# x = ((b + 2 * a) - 2 > c) or not (b < a + c / 5) and (c > b * 3-a)
# print(x)

# Question 4

# (a + b*(c - d) / 2) + (e / 7 + (f / 20))

# 1.	(a + b*(c - d) / 2) is our first part, subtract d from c
# 2.	Multiply outcome with b
# 3.	Divide result by 2
# 4.	Add result to a
# 5.	(e / 7 + (f / 20)) is our second part, Divide f by 20
# 6.	Divide e by 7
# 7.	Add results with each other
# 8.	Add results from first and second part with each other

# Question 5

# def process_employee_performance(employee_data):
#     # Upload the data we need from dictionary
#     employee_name = employee_data["name"]
#     employee_salary = employee_data["salary"]
#
#     # Use sum function to total salary of employees
#     total_salary = sum(employee_salary)
#     # Use len function to check the amount of employees, and divide total salary by it, in order to find average salary
#     average_salary = total_salary / len(employee_salary)
#
#     # Then we place employee_name as 1st index of array which is 0, average_salary as 2nd index of array which is 1
#     employee_info = [employee_name, average_salary]
#     return f"Employee: {employee_info[0]}, Average Salary: {employee_info[1]}"

# Question 6

# import tkinter as tk
#
# class YourGUIApplication():
#     def __init__(self, master):
#         # Your code here
#         self.master = master
#         self.master.title("Your GUI Application")
#
#         self.label = tk.Label(self.master, text="Hello, tkinter!")
#         self.label.pack()
#
#         self.button = tk.Button(self.master, text="Click Me", command=self.on_button_click)
#         self.button.pack()
#
#     def on_button_click(self):
#         # Your code here
#         self.label.config(text="Clicked")
#         pass
#
#
# if __name__ == "__main__":
#     root = tk.Tk()
#     app = YourGUIApplication(root)
#     root.geometry("300x50")
#     root.mainloop()

# Question 7

# Functional Library System
#
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#
# class Library:
#     def __init__(self):
#         self.books = []
#
#     def add_book(self, title, author):
#         book = Book(title, author)
#         self.books.append(book)
#
#
#     def display_books(self):
#         for book in self.books:
#             print(f"Title: {book.title}, Author: {book.author}")
#
#
# def main():
#     library = Library()
#
#     library.add_book("The Catcher in the Rye", "J.D. Salinger")
#     library.add_book("To Kill a Mockingbird", "Harper Lee")
#     library.add_book("1984", "George Orwell")
#
#     library.display_books()
#
#
# if __name__ == "__main__":
#     main()

# # Question 8

# def find_max_min(numbers):
#     max_value = float('-inf')
#     min_value = float('inf')
#
#     for num in numbers:
#         if num > max_value:
#             max_value = num
#         if num < min_value:
#             min_value = num
#
#     return min_value, max_value
#
#
# # Example usage:
# data = [15, 7, 28, 12, 35]
# result = find_max_min(data)
# print(f"Minimum value: {result[0]}, Maximum value: {result[1]}")
#
#
