class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()                          # Sort coins for early stopping
        dp = [0] * (amount + 1)               # dp[i] = min coins needed for amount i

        for i in range(1, amount + 1):
            minn = float('inf')               # Initialize minimum coins

            for coin in coins:
                diff = i - coin
                if diff < 0:                  # No need to check larger coins
                    break
                minn = min(minn, 1 + dp[diff])  # Choose the best option

            dp[i] = minn                      # Store minimum coins for amount i

        if dp[amount] < float('inf'):
            return dp[amount]                 # Solution exists
        else:
            return -1                         # Impossible to make the amount