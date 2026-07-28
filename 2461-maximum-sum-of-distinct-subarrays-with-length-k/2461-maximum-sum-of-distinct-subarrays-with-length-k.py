class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq={}
        maxi=0
        right=0
        left=0
        sumi=0
        for right in range (len(nums)):
            freq[nums[right]]=freq.get(nums[right],0)+1
            sumi+=nums[right]
            while right-left+1>k:
                freq[nums[left]]-=1
                if freq[nums[left]]==0:
                    del freq[nums[left]]
                sumi-=nums[left]
                left+=1
            if len(freq)==k:
                maxi=max(maxi,sumi)
        return maxi
            
            
