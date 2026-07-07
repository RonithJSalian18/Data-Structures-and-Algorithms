class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        l = 0
        count = 0

        for i in range(len(nums) - 1):
            nxt = nums[i] + 1
            if nums[i + 1] == nxt:
                count += 1
                l = max(l, count)
            elif nums[i] == nums[i+1]:
                continue
            else:
                count = 0
                continue

        return l + 1
                