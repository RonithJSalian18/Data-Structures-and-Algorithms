class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Start filling from the last index
        last = m + n - 1

        # Merge from the end while both arrays have elements
        while m > 0 and n > 0:
            if nums1[m - 1] < nums2[n - 1]:
                nums1[last] = nums2[n - 1]
                n -= 1
            else:
                nums1[last] = nums1[m - 1]
                m -= 1
            last -= 1

        # Copy remaining elements from nums2 (if any)
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1