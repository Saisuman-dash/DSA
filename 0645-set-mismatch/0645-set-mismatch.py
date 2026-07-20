class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        seen={}
        ans=[0]*2
        duplicate=0
        for i in range (n):
            if nums[i] in seen:
                duplicate=nums[i]
                ans[0]=duplicate
            seen[nums[i]]=seen.get(nums[i],0)+1
        for i in range (1,n+1):
            if i not in seen:
                ans[1]=i
        return ans




            

        
        
     

            

            