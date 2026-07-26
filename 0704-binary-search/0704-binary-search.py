class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        def bs(low,high,nums):
            mid=(high+low)//2
            if low>high:
                return -1
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                low=mid+1
                return bs(low,high,nums)
            elif nums[mid]>target:
                high=mid-1
                return bs(low,high,nums)   
        ans=bs(0,n-1,nums)
        return ans

            