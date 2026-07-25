class Solution:
    def maxProduct(self, n: int) -> int:
        nums = list(str(n))
        maxx = 0

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                product = int(nums[i]) * int(nums[j])
                maxx = max(maxx, product)

        return maxx
        