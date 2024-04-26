def diagonal_sum(matrix):
    # define an empty list
    value = []
    # for loop to loop through the row
    for i in range(len(matrix)):
        for j in range(len(matrix[i])): # keep the loop going in the column
            # if i and j matches append the diagonal element to the list
            if i == j:
                value.append(matrix[i][j])
    return sum(value)

M = [[1, 2, 9],
     [8, 27, 64],
     [6, 3, 1]]

print(diagonal_sum(M))
