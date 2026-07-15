class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        even = odd = 0

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        for i in range(1, (n * 2 ) + 1):
            if i % 2 == 0:
                even += i
            else:
                odd += i

        return gcd(odd, even)

        
        