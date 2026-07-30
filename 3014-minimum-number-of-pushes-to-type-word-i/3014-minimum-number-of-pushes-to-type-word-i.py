class Solution:
    def minimumPushes(self, word: str) -> int:
        add = 1
        res = 0

        for i in range(1, len(word) + 1):
            res += add
            if i % 8 == 0:
                add += 1

        return res
