class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count frequency of each task
        count = Counter(tasks)
        # Max heap using negative frequencies
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        time = 0
        q = deque()  # Stores [remaining_count, available_time]
        # Process until all tasks are completed
        while maxHeap or q:
            time += 1
            # Execute the most frequent available task
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)  # Decrease frequency
                if cnt:
                    q.append([cnt, time + n])     # Put on cooldown
            # Move cooled-down task back to the heap
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time