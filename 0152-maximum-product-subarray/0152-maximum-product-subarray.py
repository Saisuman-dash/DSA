class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxprod,minprod=1,1
        v1,v2,v3=0,0,0
        res=float('-inf')
        for i in range (len(nums)):
            v1=nums[i]
            v2=maxprod*nums[i]
            v3=minprod*nums[i]
            maxprod=max(v1,v2,v3)
            minprod=min(v1,v2,v3)
            res=max(res,maxprod,minprod)
        return res
