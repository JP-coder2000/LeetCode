def sortedSquaredArray(array):
    sortedSquares = []
    for i in array:
        sortedSquares.append(i*i)
    sortedSquares.sort()
    return sortedSquares


array = [1, 2, 3, 5, 6, 8, 9]

print(sortedSquaredArray(array))