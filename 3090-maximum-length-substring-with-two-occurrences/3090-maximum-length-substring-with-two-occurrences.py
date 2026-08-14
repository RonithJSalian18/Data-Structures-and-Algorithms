class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        hashMap = {}
        
        maxi = 0
        l = 0
        for r in range(len(s)):
            hashMap[s[r]] = hashMap.get(s[r], 0) + 1

            while hashMap[s[r]] >= 3:
                hashMap[s[l]] -= 1
                l += 1

            maxi = max(maxi, r - l + 1)

        return maxi
