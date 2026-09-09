class Solution:
    def reverseWords(self, s: str) -> str:
        arr = list(s.split())
        arr = arr[::-1]
        return " ".join(arr)