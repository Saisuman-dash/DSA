class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pt=0
        for j in range(0,len(nums)):
            if nums[j]!=0:
                nums[pt],nums[j]=nums[j],nums[pt]
                pt+=1


            
            







        # pt=-1
        # if len(nums)==1:
        #     return nums
        # for i in range(len(nums)):
        #     if nums[i]==0:
        #         pt=i
        #         break
        # if pt==-1:
        #     return nums
        # for i in range(pt,len(nums)):
        #     if nums[i]!=0 :
        #         nums[i],nums[pt]=nums[pt],nums[i]
        #         pt+=1
        # return nums


      
            
            

