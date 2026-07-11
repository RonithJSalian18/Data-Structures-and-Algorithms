class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)                               # Count character frequencies
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)                           # Build max heap

        prev = None                                      # Previously used character
        res = ""

        while maxHeap or prev:
            if prev and not maxHeap:                     # No valid character left
                return ""

            cnt, char = heapq.heappop(maxHeap)           # Get most frequent character
            res += char
            cnt += 1                                     # Decrease remaining count

            if prev:
                heapq.heappush(maxHeap, prev)            # Reinsert previous character
                prev = None

            if cnt != 0:
                prev = [cnt, char]                       # Hold current character

        return res