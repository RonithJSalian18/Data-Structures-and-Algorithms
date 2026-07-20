from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def works(k):                              # Check if speed k is sufficient
            hours = 0
            for p in piles:
                hours += ceil(p / k)               # Hours needed for this pile
            return hours <= h                      # Can finish within h hours?

        l, r = 1, max(piles)                       # Search range of eating speeds
        while l < r:
            k = (l + r) // 2                       # Middle eating speed
            if works(k):
                r = k                              # Try a smaller valid speed
            else:
                l = k + 1                          # Increase the speed

        return l                                   # Minimum valid eating speed