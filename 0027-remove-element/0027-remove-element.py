class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        pt=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[pt]=nums[i]
                pt+=1
        return pt


        # n=len(nums)
        # i=0
        # while i<n:
        #     if nums[i]==val:
        #         nums.pop(i)
        #         n-=1
        #     else:
        #         i+=1

        # return len(nums)