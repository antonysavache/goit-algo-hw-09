import time
from typing import Dict

def find_coins_greedy(amount: int) -> Dict[int, int]:
    """
    Greedy algorithm to find coins needed for change.

    Args:
        amount: The amount to make change for

    Returns:
        Dictionary with coin denominations as keys and counts as values
    """
    coins = [50, 25, 10, 5, 2, 1]
    result = {}

    for coin in coins:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count

        if amount == 0:
            break

    return result

def find_min_coins(amount: int) -> Dict[int, int]:
    """
    Dynamic programming approach to find minimum coins needed for change.

    Args:
        amount: The amount to make change for

    Returns:
        Dictionary with coin denominations as keys and counts as values
    """
    coins = [50, 25, 10, 5, 2, 1]
    # Initialize dp array with infinity except for 0
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    # Track which coin was used for each amount
    coin_used = [0] * (amount + 1)

    # Fill dp array
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    # Reconstruct the solution
    result = {}
    current_amount = amount

    while current_amount > 0:
        coin = coin_used[current_amount]
        result[coin] = result.get(coin, 0) + 1
        current_amount -= coin

    return result

def compare_algorithms(amount: int) -> None:
    """
    Compare the performance of both algorithms for a given amount.

    Args:
        amount: The amount to make change for
    """
    # Test greedy algorithm
    start_time = time.time()
    greedy_result = find_coins_greedy(amount)
    greedy_time = time.time() - start_time

    # Test dynamic programming algorithm
    start_time = time.time()
    dp_result = find_min_coins(amount)
    dp_time = time.time() - start_time

    print(f"\nAmount: {amount}")
    print(f"Greedy Result: {greedy_result}")
    print(f"Greedy Time: {greedy_time:.6f} seconds")
    print(f"DP Result: {dp_result}")
    print(f"DP Time: {dp_time:.6f} seconds")

# Test the algorithms with different amounts
def run_tests():
    test_amounts = [113, 1000, 10000, 100000]

    for amount in test_amounts:
        compare_algorithms(amount)

if __name__ == "__main__":
    run_tests()