class Solution:
    def trap(self, height: List[int]) -> int:
        # lwall keeps track of the tallest bar seen from the left so far
        # rwall keeps track of the tallest bar seen from the right so far
        lwall = rwall = 0
        n = len(height)
        
        # Arrays to store the maximum boundary walls for each index
        max_left = [0] * n
        max_right = [0] * n

        # PASS 1: Precompute the max left and max right walls for every index.
        # We do this in a single loop to save time, traversing from both ends simultaneously.
        for i in range(n):
            # j is the corresponding index from the right side.
            # When i=0, j=-1 (last element). When i=1, j=-2 (second to last), etc.
            j = -i - 1 
            
            # Record the highest wall seen SO FAR to the left of i
            max_left[i] = lwall
            
            # Record the highest wall seen SO FAR to the right of j
            max_right[j] = rwall
            
            # Update our running maximums for the next iteration
            # If the current bar is taller than our current wall, it becomes the new wall
            lwall = max(lwall, height[i])
            rwall = max(rwall, height[j])

        # PASS 2: Calculate the trapped water
        summ = 0
        for i in range(n):
            # The water level at this index is determined by the shorter of the two bounding walls
            pot = min(max_left[i], max_right[i])
            
            # The actual water trapped is the water level minus the height of the current bar.
            # We use max(0, ...) because if the bar is taller than the bounding walls, 
            # it traps 0 water (we can't have negative water).
            summ += max(0, pot - height[i])

        return summ