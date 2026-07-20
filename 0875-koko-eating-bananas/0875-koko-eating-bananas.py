class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)              # Search range of possible eating speeds
        res = r                           # Store the minimum valid speed found

        while l <= r:
            k = (l + r) // 2              # Try the middle eating speed
            hours = 0

            for p in piles:
                hours += ceil(p / k)      # Hours needed to finish this pile

            if hours <= h:                # Can finish within h hours
                r = k - 1                 # Search for a smaller valid speed
                res = min(res, k)         # Update the answer
            else:
                l = k + 1                 # Speed is too slow, increase it

        return res                        # Minimum eating speed