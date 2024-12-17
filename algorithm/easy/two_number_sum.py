## Two Number Sum
# Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. If any two numbers in the input array sum up to the
# target sum, the function should return them in an array, in any order. If no two numbers sum up to the target sum, the function should return an empty array.
# Note that the target sum has to be obtained by summing two different integers in the array; you can't add a single integer to itself in order to obtain the target sum.
#
# You can assume that there will be at most one pair of numbers summing up to the target sum.


# def twoNumberSum(array, targetSum):
#     for i in range(len(array)):
#         for j in range(i + 1, len(array)):
#             if array[i] + array[j] == targetSum:
#                 return [array[i], array[j]]
#     return []

def two_number_sum(array, targetSum):
    nums = {}  # Dictionary to store potential matches
    for num in array:
        # Calculate the complement of the current number
        potential_match = targetSum - num
        # Check if the complement exists in the dictionary
        if potential_match in nums:
            return [potential_match, num]
        # Otherwise, add the number to the dictionary
        nums[num] = True
    return []  # Return an empty list if no pair is found
