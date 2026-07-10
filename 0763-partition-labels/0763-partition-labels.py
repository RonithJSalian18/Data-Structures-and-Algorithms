class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Store the last occurrence of each character
        last = {}
        for i, ch in enumerate(s):
            last[ch] = i

        res = []
        size = end = 0

        for i, ch in enumerate(s):
            size += 1                     # Increase current partition size
            end = max(end, last[ch])      # Update partition end

            if i == end:                  # Partition completed
                res.append(size)
                size = 0                  # Reset size for next partition

        return res