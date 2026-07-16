class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        i=1
        bestend=nums[0]
        ans=nums[0]
        n=len(nums)
        sum=0
        ansnor=nums[0]
        ansrev=nums[0]
        for i in range (0,n):
            sum = sum+nums[i]
        for i in range (1,n):
            v1=nums[i]
            v2=bestend+nums[i]
            bestend=max(v1,v2)
            ansnor=max(ansnor,bestend)
        bestend=nums[0]
        for i in range (1,n):
            v1=nums[i]
            v2=bestend+nums[i]
            bestend=min(v1,v2)
            ansrev=min(ansrev,bestend)
        if ansnor<0:
            return ansnor
        ansrev=sum-ansrev
        ans=max(ansnor,ansrev)
        return ans