class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0           # Min and max possible open brackets

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1  # '*' as ')' or '('

            if leftMax < 0:               # Too many closing brackets
                return False

            if leftMin < 0:
                leftMin = 0               # Minimum open count can't be negative

        return leftMin == 0               # All opens can be matched