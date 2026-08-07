class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        net=sum(nums)
        sumleft=0
        sumright=0
        for i in range (0,len(nums)):
            sumright=net-(sumleft+nums[i])
            if sumleft==sumright:
                return i
            sumleft+=nums[i]

        return -1
