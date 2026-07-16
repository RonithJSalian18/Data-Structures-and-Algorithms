class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        mx = float("-inf")

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        res = []
        for n in nums:
            mx = max(n, mx)
            res.append(gcd(mx, n))

        res.sort()
        s = 0
        i, j = 0, len(res) - 1
        while i < j:
            s += gcd(res[i], res[j])
            i += 1
            j -= 1

        return s