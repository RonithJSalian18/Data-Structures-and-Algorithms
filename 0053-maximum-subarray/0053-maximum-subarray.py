class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        curSum = 0
        
        for n in nums:
            if curSum < 0:
                curSum = 0
            
            curSum += n
            maxi = max(curSum, maxi)

        return maxi