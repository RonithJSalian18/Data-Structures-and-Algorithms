class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        # dp stores the answer for each state (i, total)
        # (i, total) -> number of ways to reach the target
        dp = {}

        # i = current index in nums
        # total = current sum obtained so far
        def backtrack(i, total):
            # Base case:
            # We have processed all numbers
            if i == len(nums):
                # If current sum equals target,
                # this is one valid way
                # Otherwise, it is not a valid way
                return 1 if total == target else 0
            # If we have already calculated this state,
            # return the stored result instead of recalculating
            if (i, total) in dp:
                return dp[(i, total)]

            # We have 2 choices for nums[i]:
            #
            # 1. Add nums[i] to total
            # 2. Subtract nums[i] from total
            #
            # Add the number of valid ways from both choices
            dp[(i, total)] = (
                backtrack(i + 1, total + nums[i]) +
                backtrack(i + 1, total - nums[i])
            )

            # Return the number of ways for this state
            return dp[(i, total)]

        # Start from index 0 with sum 0
        return backtrack(0, 0)