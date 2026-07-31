class Solution:
    def minimumPushes(self, word: str) -> int:
        hashMap = {}

        for ch in word:
            if ch not in hashMap:
                hashMap[ch] = 1
            else:
                hashMap[ch] += 1

        sortedFreq = sorted(hashMap.values(), reverse=True)

        res = 0

        for i, freq in enumerate(sortedFreq):
            presses = i // 8 + 1
            res += presses * freq

        return res