class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count=0
       
        right=0
        left=0
        prod=1
        for right in range(len(nums)):
            prod*=nums[right]
            if prod<k:
                count+=right-left+1 
            while prod>=k and left<right:
                prod=prod//nums[left]
                left+=1
                if prod<k:
                    count+=right-left+1
        return count
            