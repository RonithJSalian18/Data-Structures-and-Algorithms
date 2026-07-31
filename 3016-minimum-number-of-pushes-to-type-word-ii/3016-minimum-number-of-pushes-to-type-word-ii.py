class Solution:
    def minimumPushes(self, word: str) -> int:
        hashMap = {}

        for ch in word:
            if ch not in hashMap:
                hashMap[ch] = 1
            else:
                hashMap[ch] += 1

        sortedDict = dict(sorted(hashMap.items(), key=lambda x: x[1], reverse=True))
        
        res = 0
        count = 0

        for char, freq in sortedDict.items():
            add = count // 8 + 1

            while freq > 0:
                res += add
                freq -= 1
            count += 1

        return res