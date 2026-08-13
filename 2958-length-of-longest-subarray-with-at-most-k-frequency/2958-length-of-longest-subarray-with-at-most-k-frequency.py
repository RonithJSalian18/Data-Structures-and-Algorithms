class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        count = {}
        l = 0
        maxi = 0

        for r in range(len(nums)):
            count[nums[r]] = count.get(nums[r], 0) + 1

            # nums[r] appears more than k times
            while count[nums[r]] > k:
                count[nums[l]] -= 1
                l += 1

            maxi = max(maxi, r - l + 1)

        return maxi