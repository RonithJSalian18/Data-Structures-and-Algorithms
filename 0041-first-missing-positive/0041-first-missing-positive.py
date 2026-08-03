class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0                      # Ignore negative numbers

        for i in range(len(nums)):
            val = abs(nums[i])                  # Current value

            if 1 <= val <= len(nums):           # Only valid range matters
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1         # Mark as present
                if nums[val - 1] == 0:
                    nums[val - 1] = -(len(nums) + 1)  # Mark zero as visited

        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0:                # Not marked → missing
                return i

        return len(nums) + 1                    # All 1...n are present