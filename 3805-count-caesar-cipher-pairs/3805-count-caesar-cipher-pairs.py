from collections import defaultdict

class Solution:
    def countPairs(self, words: List[str]) -> int:
        freq = defaultdict(int)
        res = 0

        for word in words:
            first = ord(word[0]) - ord('a')

            pattern = []

            for ch in word:
                diff = (ord(ch) - ord('a') - first) % 26
                pattern.append(diff)

            pattern = tuple(pattern)

            res += freq[pattern]
            freq[pattern] += 1

        return res