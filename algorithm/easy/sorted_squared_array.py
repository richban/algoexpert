# Sorted Squared Array ☆
# Write a function that takes in a non-empty array of integers that are sorted in ascending order and returns a new array of the same length with the squares of the
# original integers also sorted in ascending order.

# def sortedSquaredArray(array):
#     # NOTE: integers! can be negative!
#     return list(map(lambda x: x**2, array))

def sortedSquaredArraySuboptimal(array):
    # O(n) + O(nlogn) => O(nlogn) time | O(n) space
    output = []
    for value in array:
        output.append(value**2)

    return sorted(output) # this is On2

def sortedSquaredArray(array):
    # O(n) time | O(n) space
    output = [0] * len(array)
    startIdx = 0
    endIdx = len(array) - 1
    outputIdx = len(array) - 1  # Initialize output index at the last position

    # Loop until start index is less than or equal to end index
    while startIdx <= endIdx:
        if abs(array[startIdx]) < abs(array[endIdx]):
            output[outputIdx] = array[endIdx] ** 2
            endIdx -= 1
        else:
            output[outputIdx] = array[startIdx] ** 2
            startIdx += 1
        outputIdx -= 1  # Decrement the output index to fill the next position in the next iteration

    return output

