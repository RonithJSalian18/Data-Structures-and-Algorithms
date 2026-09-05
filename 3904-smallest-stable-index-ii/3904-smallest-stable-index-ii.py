class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        suffix = [0] * n

        mini = float('inf')
        for i in range(n - 1, -1, -1):
            mini = min(mini, nums[i])
            suffix[i] = mini

        maxi = 0
        for i in range(n):
            maxi = max(maxi, nums[i])
            score = maxi - suffix[i]
            if score <= k:
                return i

        return -1