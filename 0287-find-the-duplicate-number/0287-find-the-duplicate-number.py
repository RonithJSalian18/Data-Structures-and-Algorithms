class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Find the meeting point of slow and fast pointers
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: Find the entrance to the cycle (duplicate number)
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow