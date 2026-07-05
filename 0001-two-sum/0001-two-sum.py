class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            hashMap[nums[i]] = i

        for i in range(len(nums)):
            val = target - nums[i]

            if val in hashMap and hashMap[val] != i:
                return [i, hashMap[val]]