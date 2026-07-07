class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            elif i>0 and nums[i] == nums[i-1]:
                continue

            l, h = i+1, n-1
            while l < h:
                summ = nums[i] + nums[h] + nums[l]
                if summ == 0:
                    res.append([nums[i], nums[l] , nums[h]])
                    l+=1 
                    h-=1

                    while l < h and nums[l] == nums[l-1]:
                        l += 1
                    while l < h and nums[h] == nums[h+1]:
                        h -= 1

                elif summ < 0:
                    l += 1
                else:
                    h -= 1
        return res