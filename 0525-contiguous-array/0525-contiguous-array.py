class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i]==0:
                nums[i]=-1
        left=0
        sumi=0
        freq={0:-1}
        maxi=0
        for right in range(len(nums)):
            sumi+=nums[right]
            if sumi in freq:
                maxi=max(maxi,right-freq[sumi])
            else:
                freq[sumi]=right
        return maxi
        
            
            