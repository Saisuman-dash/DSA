class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedset= sorted(nums)
        ans=[0]*len(nums)
        hash={}
        for i in range (len(sortedset)):
            if sortedset[i] not in hash:
                hash[sortedset[i]]=i
        for i in range (len(nums)):
            ans[i]=hash[nums[i]]
        return ans

            
