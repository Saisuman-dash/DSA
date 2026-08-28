class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def first(l,r):
            ans=-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    ans=mid
                    r=mid-1
                elif (nums[mid]<target):
                    l=mid+1
                elif (nums[mid]>target):
                    r=mid-1
            return ans
        def last(l,r):
            ans=-1
            while l<=r:
                mid=(l+r)//2
                if nums[mid]==target:
                    ans=mid
                    l=mid+1
                elif (nums[mid]<target):
                    l=mid+1
                elif (nums[mid]>target):
                    r=mid-1
            return ans
        leftmost=first(0,len(nums)-1)
        rightmost=last(0,len(nums)-1)
        return [leftmost,rightmost]