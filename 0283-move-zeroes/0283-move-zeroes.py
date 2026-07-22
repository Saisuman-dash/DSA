class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pt=-1
        if len(nums)==1:
            return nums
        for i in range(len(nums)):
            if nums[i]==0:
                pt=i
                break
        if pt==-1:
            return nums
        for i in range(pt,len(nums)):
            if nums[i]!=0 :
                nums[i],nums[pt]=nums[pt],nums[i]
                pt+=1
        return nums


      
            
            

