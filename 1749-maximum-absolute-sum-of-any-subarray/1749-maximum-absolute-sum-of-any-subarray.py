class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        bestend=nums[0]
        ans=nums[0]
        ansmax=nums[0]
        ansmin=nums[0]
        bestendmax=nums[0]
        bestendmin=nums[0]
        n=len(nums)
        for i in range(1,n):
            v1=nums[i]
            v2=bestendmax+nums[i]
            bestendmax=max(v1,v2)
            ansmax=max(ansmax,bestendmax)

            v1=nums[i]
            v2=bestendmin+nums[i]
            bestendmin=min(v1,v2)
            ansmin=min(ansmin,bestendmin)

            ans=max(ansmax,abs(ansmin))
        if ansmax<0:
            return abs(ansmax)

        return ans