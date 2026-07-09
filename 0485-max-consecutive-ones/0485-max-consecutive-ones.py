class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        c = 0
        
        for n in nums:
            if n == 1:
                c += 1
                count = max(c, count)
            else:
                c = 0

        return count
        