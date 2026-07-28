class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s
        m = n // 2
        res = ''

        if n % 2 == 0:
            half = s[:m]
            sort = "".join(sorted(half))
            res = sort + sort[::-1]
        else:
            mid = s[m]
            half = s[:m]
            sort = "".join(sorted(half))
            res = sort + mid + sort[::-1]
            
        return res
        