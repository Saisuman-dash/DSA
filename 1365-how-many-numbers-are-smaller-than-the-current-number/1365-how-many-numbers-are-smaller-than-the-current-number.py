class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedset= sorted(nums)
        ans=[0]*len(nums)
        for i in range (len(nums)):
            ans[i]=sortedset.index(nums[i])
        return ans