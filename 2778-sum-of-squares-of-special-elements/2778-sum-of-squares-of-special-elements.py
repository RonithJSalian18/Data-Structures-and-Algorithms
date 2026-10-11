class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i, cur in enumerate(nums, start=1):
            if n % i == 0:
                res += cur * cur
        return res
        