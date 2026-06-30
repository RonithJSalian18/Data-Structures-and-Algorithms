from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        i = n - 2
        
        # Step 1: Find the first decreasing element from the right
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
            
        # Step 2: If we found a decreasing element, find the next largest to swap it with
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Swap them
            nums[i], nums[j] = nums[j], nums[i]
            
        # Step 3: Reverse the suffix starting at i + 1
        nums[i+1:] = reversed(nums[i+1:])