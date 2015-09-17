import random


array = [[random.randint(0, 3) for i in range(3)] for i in range(5)]
row = [0 for i in range(len(array))]
col = [0 for i in range(len(array[0]))]

for ele in array:
    print(ele)
print('\n')

# mark locations where there's a 0
for i in range(len(array)):
    for j in range(len(array[0])):
        if array[i][j] == 0:
            row[i] = 1
            col[j] = 1

# if there's a 0 at either the column or row, set the value to 0
for i in range(len(array)):
    for j in range(len(array[0])):
        if row[i] == 1 or col[j] == 1:
            array[i][j] = 0


for row in array:
    print(row)
