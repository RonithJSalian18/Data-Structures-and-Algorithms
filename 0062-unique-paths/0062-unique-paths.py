class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create DP table
        dp = []
        for _ in range(m):
            dp.append([0] * n)

        # Starting cell
        dp[0][0] = 1

        # Fill DP table
        for i in range(m):
            for j in range(n):
                # Skip the starting cell
                if i == j == 0:
                    continue

                val = 0

                # Add paths from above
                if i > 0:
                    val += dp[i - 1][j]

                # Add paths from left
                if j > 0:
                    val += dp[i][j - 1]

                # Store total paths
                dp[i][j] = val

        # Return paths to bottom-right cell
        return dp[m - 1][n - 1]