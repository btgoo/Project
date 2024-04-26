# Mock questions

#1. a.
# a = [11, 18, 3, 14, 90, 42, 73, 7, 3, 43]
#
# def insertion_sort(arr):
#     for i in range(1, len(arr)): # i is the index of the key we want to insert
#         key = arr[i]
#         j = i - 1 # index to iterate over sorted elements
#         while j >= 0 and key < arr[j]: # when conditions are broken, correct spot for key is found
#             arr[j + 1] = arr[j] # moving element over to make space
#             j -= 1 # iterating from right to left of sorted list
#         arr[j + 1] = key
#     return arr
#
# print(insertion_sort(a))

# b.

# Average time complexity of insertion sort is O(n^2) because each element may be compared with other elements including
# already sorted ones.

# 2

# def bubble_sort(arr):
#     n = len(arr)  # Get the length of the array
#
#     # Iterate through each element of the array
#     for i in range(n): # Iterate through each element up to the last unsorted element
#         # The last 'i' elements are already sorted in each pass
#         for j in range(0, n - i - 1): # Compare adjacent elements, and removes already sorted elements
#             if arr[j] > arr[j + 1]: # Swap elements if they are in the wrong order
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr  # Return the sorted array
#
# arr = [18, 28, 7, 16, 2, 9, 1, 30]
# print(bubble_sort(arr))

# b.

# Bubble Sort has an average-case time complexity of O(n^2), making it inefficient for large datasets.
# Merge Sort has an average-case time complexity of O(n log n), making it much more efficient, particularly for large
# datasets.

#5.

# intervals = [(9, 10), (10, 11), (10.5, 11.5), (11, 12), (11.5, 12.5)]
#
#
# def get_end_time(meeting):
#     return meeting[1]
#
#
# def interval_scheduling(intervals):
#
#     intervals.sort(key=get_end_time)
#
#     selected_intervals = []
#     last_end_time = float('-inf')
#
#     for meeting in intervals:
#         start_time, end_time = meeting
#
#         if start_time >= last_end_time:
#             selected_intervals.append(meeting)
#             last_end_time = end_time
#
#     return selected_intervals
#
# intervals_test = [(10, 11), (9, 10), (10.5, 11.5), (11, 12), (11.5, 12.5)]
#
# print(interval_scheduling(intervals_test)

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# Calling the decorated function
say_hello()