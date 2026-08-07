class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zerocount = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                prod *= nums[i]
            else:
                zerocount += 1
        for i in range(len(nums)):
            if zerocount == 0:
                nums[i] = prod // nums[i]
            elif zerocount == 1:
                if nums[i] == 0:
                    nums[i] = prod
                else:
                    nums[i] = 0
            else:
                nums[i] = 0

        return nums