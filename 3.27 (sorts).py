# Insertion sort

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
# arr = [18, 498,89489158,949856,815,89561,88,59,1,5,984,8921]
# print(insertion_sort(arr))

# Bubble sort

# def bubble_sort(arr):
#     n = len(arr)
#
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr
#
# arr=[18, 28, 7, 16, 2, 9, 1, 30]
# print(bubble_sort(arr))

# Merge sort

# def merge_sort(arr):
#     if len(arr) > 1:
#         # dividing array
#         mid = len(arr) // 2
#         left_half = arr[:mid]
#         right_half = arr[mid:]
#         # recursive calls until all sub-arrays size 1
#         merge_sort(left_half)
#         merge_sort(right_half)
#
#         i = 0  # leftmost value of a given left array
#         j = 0  # rightmost value of a given left array
#         k = 0  # the space i and j are competing
#
#         while i < len(left_half) and j < len(right_half):
#             if left_half[i] < right_half[j]:
#                 arr[k] = left_half[i]
#                 i += 1
#             else:
#                 arr[k] = right_half[j]
#                 j += 1
#             k += 1
#
#         while i < len(left_half):
#             arr[k] = left_half[i]
#             i += 1
#             k += 1
#
#         while j < len(right_half):
#             arr[k] = right_half[j]
#             j += 1
#             k += 1
#     return arr
#
# arr = [18, 498, 89489158, 949856, 815, 89561, 88, 59, 1, 5, 984, 8921]
# print(merge_sort(arr))
