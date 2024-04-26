def bubble(array):
    for i in array:
        if array[i] > array[i + 1]:
            i = array[i]
    return i


array = [23, 1, 4, 17, 8, 9, 11, 15, 5]
print(bubble(array))