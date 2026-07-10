class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = 0
        sum=0
        avg=0
        maxi=float("-inf")
        for right in range (len(nums)):
            sum += nums[right]
            
            if right-left+1>k:
                sum = sum-nums[left]
                left+=1
            if right-left+1==k:
                avg=sum/k
                maxi = max(maxi,avg)
           
                
        return maxi
