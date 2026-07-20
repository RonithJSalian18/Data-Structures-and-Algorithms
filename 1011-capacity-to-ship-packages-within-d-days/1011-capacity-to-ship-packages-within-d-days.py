class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)        # Search range of ship capacities
        res = r                                  # Store the minimum valid capacity

        def can(capacity):
            curCap = capacity                    # Remaining capacity of current ship
            ships = 1                            # Start with one ship

            for w in weights:
                if curCap - w < 0:               # Doesn't fit, use a new ship
                    ships += 1
                    curCap = capacity            # Reset remaining capacity
                curCap -= w                      # Load the current package

            return ships <= days                 # Can ship within given days?

        while l <= r:
            capacity = (l + r) // 2              # Try the middle capacity

            if can(capacity):
                res = min(res, capacity)         # Update the answer
                r = capacity - 1                 # Try a smaller capacity
            else:
                l = capacity + 1                 # Increase the capacity

        return res                               # Minimum required ship capacity