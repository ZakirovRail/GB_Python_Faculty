matrix_list = [[31, 22, 15], [37, 43, 18], [51, 86, 26]]


def print_matrix_list(matrix_list):
    for row in range(len(matrix_list)):
        for number in range(len(matrix_list[row])):
            print('{:5d}'.format(matrix_list[row][number]), end="")
        print()

print_matrix_list(matrix_list)



# def printMatrix(matrix):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             print("{:4d}".format(matrix[i][j]), end="")
#         print()
# matrix = [[-1, 0, 1], [-1, 0, 1], [0, 1, -1], [1, 1, -1]]
# printMatrix(matrix)

