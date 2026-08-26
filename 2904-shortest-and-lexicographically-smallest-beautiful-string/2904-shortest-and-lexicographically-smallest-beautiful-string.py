class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        mini = float('inf')
        ones = 0
        beauty = ''

        l = 0

        for r in range(len(s)):
            if s[r] == '1':
                ones += 1

            while ones >= k:
                if ones == k:
                    curr = s[l:r + 1]

                    if len(curr) < mini or (len(curr) == mini and curr < beauty):
                        beauty = curr
                        mini = len(curr)

                if s[l] == '1':
                    ones -= 1

                l += 1

        return beauty