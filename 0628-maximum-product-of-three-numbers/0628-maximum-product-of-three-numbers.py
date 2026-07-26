class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        maxi = float('-inf')
        n = len(nums)

        for i in range(n - 3, n):
            prod = 1
            for d in range(3):
                prod *= nums[(i + d) % n]
            maxi = max(maxi, prod)

        return maxi