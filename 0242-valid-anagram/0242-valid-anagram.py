class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter_s = {}
        counter_t = {}

        for ch in s:
            if ch not in counter_s:
                counter_s[ch] = 1
            elif ch in counter_s:
                counter_s[ch] += 1

        for ch in t:
            if ch not in counter_t:
                counter_t[ch] = 1
            elif ch in counter_t:
                counter_t[ch] += 1

        return counter_s == counter_t