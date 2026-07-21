class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Idx = {n: i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)
        stack = []

        for cur in nums2:
            while stack and cur > stack[-1]:
                val = stack.pop()
                idx = nums1Idx[val]
                res[idx] = cur

            if cur in nums1Idx:
                stack.append(cur)

        return res