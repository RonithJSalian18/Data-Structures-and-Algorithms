class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        stk = []

        for ch in s:
            if ch not in hashMap:
                stk.append(ch)
            else:
                if not stk or stk[-1] != hashMap[ch]:
                    return False
                stk.pop()

        return not stk