class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1
        m = 0

        while l < r:
            w = r - l
            h = min(height[l], height[r])
            m = max(m, w * h)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return m



        