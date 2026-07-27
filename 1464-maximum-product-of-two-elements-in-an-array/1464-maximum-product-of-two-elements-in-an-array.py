class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = [-n for n in nums]
        
        heapq.heapify(nums)
        m1 = -heapq.heappop(nums)
        m2 = -heapq.heappop(nums)
        
        return (m1 - 1) * (m2 - 1)
        
        