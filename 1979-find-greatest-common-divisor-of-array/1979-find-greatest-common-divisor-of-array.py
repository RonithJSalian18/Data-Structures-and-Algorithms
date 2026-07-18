class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mx = max(nums)
        mn = min(nums)

        def gcd(a, b):
            while b:
                a, b, = b, a % b
            return a

        return gcd(mx, mn)        