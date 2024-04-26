# # Question 1
#
# def highest_avg(student_data):
#     averages = []
#     for student in student_data:
#         student_average = sum(student) / len(student)
#         averages.append(student_average)
#         highest = max(averages)
#         index = averages.index(highest)
#
#     return f"The student at the list {index + 1} has the highest score with {highest}"
#
# student_scores = [ [90, 85, 78],
#     [88, 92, 80],
#     [76, 89, 94],
#     [82, 79, 85]
#  ]
#
# print(highest_avg(student_scores))

# Question 2

# def cube_root():
#     number = int(input("Number: "))
#     guess = int(input("Guess: "))
#     i = 1
#     while i <= 1000:
#         guess = 1/3 * (2 * guess + number / guess ** 2)
#         i += 1
#         if guess ** 3 == number:
#             break
#     return guess
#
# print(cube_root())

# Question 3

# x = 1
# y = 10
# z = 5
#
# x = not((x+2) > z) or (x + z < -y)
# y = (y - 5 > (2 - x) + z) or not (x * z == y -5) and (-z < 3 * (y + 1))
# # The expression should evaluate to False because first part is False, second part is False and third part is also False too
#
# print(x)
# print(y)

# a = 1
# b = 2
# c = 3
# d = 4
# e = 5
# f = 6
# x = (a * b * (c - d) ** 2) + ((e + f) / 2)
# print(x)

# import math
#
# print(math.sqrt(64))
# Question 4
# def function():
#
#     x = int(input("Enter the value of x: "))
#     result = 2 * x ** 2 - 4 * x + 7
#
#     return result
#
# print(function())

# Question 6
#
import tkinter as tkinter
class GUIApplication:
    def __init__(self, master):
        self.master = master
        master.title("Simple GUI Application")

        self.label = tkinter.Label(master, text="Hello, tkinter!")
        self.label.pack()

        # Your code here
        self.button = tkinter.Button(master, text="Click me",command=self.on_button_click)
        self.button.pack()

    def on_button_click(self):
        self.label.config(text="Button clicked")

        pass

if __name__ == "__main__":
    root = tkinter.Tk()
    app = GUIApplication(root)
    root.mainloop()

# Question 7

# Functional Kids DVD Library

# class Library:
#     def __init__(self):
#         self.library = []
#
#     def add_kids_dvd(self, title, director, age_rating):
#         kids_dvd = {"title": title, "director": director, "age_rating": age_rating}
#         self.library.append(kids_dvd)
#
#     def display_kids_dvds(self):
#         for kids_dvd in self.library:
#             print(f"Title: {kids_dvd['title']}, Director: {kids_dvd['director']}, Age Rating: {kids_dvd['age_rating']}")
#
# def main():
#     kids_dvd_library = Library()
#
#     Library.add_kids_dvd(kids_dvd_library, "Frozen", "Chris Buck, Jennifer Lee", "G")
#     Library.add_kids_dvd(kids_dvd_library, "Toy Story", "John Lasseter", "G")
#     Library.add_kids_dvd(kids_dvd_library, "Moana", "Ron Clements, John Musker", "PG")
#
#     print("Kids DVDs in the library:")
#     Library.display_kids_dvds(kids_dvd_library)
#
# if __name__ == "__main__":
#     main()


# # Question 8
#
# def find_max_and_average(numbers):
#     max_value = float('-inf')
#     total_sum = 0
#     for num in numbers:
#         if num > max_value:
#             max_value = num
#         total_sum += num
#
#     average_value = total_sum / len(numbers)
#     return max_value, average_value
#
# data = [15, 7, 28, 12, 35]
# result = find_max_and_average(data)
#
# print(f"Maximum value: {result[0]}, Average value: {result[1]}")



