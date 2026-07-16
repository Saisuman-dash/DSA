class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxend=nums[0]
        minend=nums[0]
        ans=nums[0]
        n=len(nums)
        for i in range(1,n):
            v1=nums[i]
            v2=nums[i]*maxend
            v3=nums[i]*minend
            maxend=max(v1,v2,v3)
            minend=min(v1,v2,v3)
            ans=max(ans,maxend,minend)
        return ans