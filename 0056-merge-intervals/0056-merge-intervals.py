class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals by start time
        intervals.sort(key=lambda i: i[0])

        # Start with the first interval
        output = [intervals[0]]

        # Iterate through remaining intervals
        for start, end in intervals[1:]:
            # End of the last merged interval
            lastEnd = output[-1][1]

            # If intervals overlap, merge them
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                # No overlap, add new interval
                output.append([start, end])

        # Return merged intervals
        return output