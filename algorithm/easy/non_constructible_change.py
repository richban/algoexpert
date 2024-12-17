# Given an array of positive integers representing the values of coins in your possession, write a function that returns the minimum amount of change (the minimum
# sum of money) that you cannot create. The given coins can have any positive integer value and aren't necessarily unique (i.e., you can have multiple coins of the
# same value).
# For example, if you're given coins = [1, 2, 5], the minimum amount of change that you can't create is 4. If you're given no coins, the minimum amount of
# change that you can't create is 1.

def nonConstructibleChangeBruteForce(coins):
    """Brute Force.

    O(2^n) time
    O(2^n) space

    Start: possible_sums = {0}
    Adding coin 1:
    From 0 + 1 = 1 ➔ possible_sums = {0, 1}
    Adding coin 2:
    From 0 + 2 = 2 ➔ possible_sums = {0, 1, 2}
    From 1 + 2 = 3 ➔ possible_sums = {0, 1, 2, 3}
    Adding coin 5:
    From 0 + 5 = 5 ➔ possible_sums = {0, 1, 2, 3, 5}
    From 1 + 5 = 6 ➔ possible_sums = {0, 1, 2, 3, 5, 6}
    From 2 + 5 = 7 ➔ possible_sums = {0, 1, 2, 3, 5, 6, 7}
    From 3 + 5 = 8 ➔ possible_sums = {0, 1, 2, 3, 5, 6, 7, 8}

    """
    if not coins:  # Check if the list of coins is empty
        return 1

    # Generate all possible sums of coins
    possible_sums = set([0])  # Start with 0 which represents using no coins

    # Loop through each coin and update the possible sums set
    for coin in coins:
        current_sums = list(possible_sums)  # Create a snapshot of current sums
        for sum_value in current_sums:
            new_sum = sum_value + coin
            possible_sums.add(new_sum)

    # Find the smallest sum that cannot be created
    smallest_non_constructible = 1  # Start checking from 1
    while True:
        if smallest_non_constructible not in possible_sums:
            return smallest_non_constructible
        smallest_non_constructible += 1


def nonConstructibleChange(coins):
    """
    Here’s the role of the variable `current_change_created`, which we set to 1 at the beginning:

    It’s like your target. You start by asking, "Can I make 1 penny with my coins?"
    You then use your coins, one by one, to try and reach this target. If you can make 1 penny,
    then you increase your target to 2 pennies, and then 3 pennies, and so on.
    This variable keeps track of the next target amount you’re trying to make.
    Whenever you add a coin to your total, you ask, "Can I now make this new target amount with the coins I’ve used so far?"
    The reason you start with 1 is simple: if you don’t have any coin at all, the smallest amount you can’t make is 1 penny,
    because you can’t make anything without coins! But as soon as you find you can make 1 penny,
    your target moves up to 2 pennies, then higher as you keep being able to make each new target amount with your coins.
    """
    # Sort the coins to ensure we handle the smallest coins first
    coins.sort()

    # Initialize the smallest amount of change that we cannot create
    current_change_created = 1

    # Process each coin in the sorted list
    for coin in coins:
        # Check if the current coin is too large to create the current smallest change
        if coin > current_change_created:
            break
        # Otherwise, add the value of the coin to the range of creatable change
        current_change_created += coin

    return current_change_created

