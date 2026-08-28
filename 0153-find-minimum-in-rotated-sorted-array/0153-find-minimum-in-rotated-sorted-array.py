class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def bs(l,r):
            
            while l<r:
                mid=(l+r)//2
                if nums[mid]>nums[r]:
                    l=mid+1
                elif nums[mid]<nums[r]:
                    r=mid
                
            return nums[l]
        ans=bs(0,len(nums)-1)
        return ans