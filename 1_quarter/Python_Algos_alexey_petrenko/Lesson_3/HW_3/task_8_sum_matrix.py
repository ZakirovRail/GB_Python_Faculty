N = 5
M = 4
matrix = []

for i in range(N):
    row = []
    summ = 0

    for j in range(M - 1):
        num = int(input(f'{i}-я строка,, {j}-ый элемент : '))
        summ += num
        row.append(num)

    row.append(summ)
    matrix.append(row)

for line in matrix:
    print(line)
