class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def bs(low,high,nums):
            mid=(low+high)//2
            if low>high:
                return low
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                low=mid+1
                return bs(low,high,nums)
            elif nums[mid]>target:
                high=mid-1
                return bs(low,high,nums)
        return bs(0,len(nums)-1,nums)
            