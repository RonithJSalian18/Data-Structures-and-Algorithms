class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0 
        s = set(nums)

        for n in s:
            if n - 1 not in s:
                nxt = n + 1
                length = 1
                while nxt in s:
                    length += 1
                    nxt += 1
                longest = max(length, longest)

        return longest
                