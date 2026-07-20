class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate=0
        missing=0
        index=0
        for num in nums:
            index=abs(num)-1
            if nums[index] > 0:
                nums[index]*= -1
            elif nums[index]<0:
                duplicate=abs(num)
            
        for i in range(len(nums)):
            if nums[i]>0:
                missing=i+1
        return [duplicate,missing]
            
        












        # n=len(nums)
        # seen={}
        # ans=[0]*2
        # duplicate=0
        # for i in range (n):
        #     if nums[i] in seen:
        #         duplicate=nums[i]
        #         ans[0]=duplicate
        #     seen[nums[i]]=seen.get(nums[i],0)+1
        # for i in range (1,n+1):
        #     if i not in seen:
        #         ans[1]=i
        # return ans




            

        
        
     

            

            