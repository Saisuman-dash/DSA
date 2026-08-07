class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi=float('-inf')
        maxs=float('-inf')
        v1=0
        v2=0
        sumi=0
        for i in range(len(nums)):
            sumi+=nums[i]
            # if sumi<0:
            #     sumi=0
            v1=nums[i]
            v2=sumi
            maxs=max(v1,v2) 
            maxi=max(maxi,maxs)
            if sumi<0:
                sumi=0
        return maxi