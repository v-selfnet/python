array = [[23,67,79,54], [56,71,98,66], [87,88,55,23], [11,77,99,44]]

# Print all array
print(array[0], array[1], array[2], array[3])
print(array[1])
print(array[2])
print(array[3])

print(array[1][1], array[1][2])

# Print value of array
print('Declared main array with loop')
for x in array:
    for y in x:
        print(y, end=' ')
    print()

# Insert Array
print('Insert 1 array in first index')
array.insert(0,[0,0,0,0])
for x in array:
    for y in x:
        print(y, end=' ')
    print()

# Update Array
print('Update index')
array[1] = [22,99]
array[2][2] = 0
for x in array:
    for y in x:
        print(y, end=' ')
    print()

# Delete Array
print('Delete 1 array ')
del array[2]
del array[4][3]
for x in array:
    for y in x:
        print(y, end=' ')
    print()

# Comprehension
num = [[i for i in range(1, j+1)] for j in range(1, 9)]
print(num)
for x in num:
     print(x)