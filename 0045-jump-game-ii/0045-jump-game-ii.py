class Solution:
    def jump(self, nums: List[int]) -> int:
        smallest = 0              # Number of jumps
        n = len(nums)
        end = far = 0             # Current range end and farthest reachable index

        for i in range(n - 1):    # No need to process the last index
            far = max(far, i + nums[i])  # Update farthest reachable position

            if i == end:          # End of current jump range
                smallest += 1     # Make another jump
                end = far         # Extend the jump range

        return smallest