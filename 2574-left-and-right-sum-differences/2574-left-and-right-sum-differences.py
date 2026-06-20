class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftSum =[0]*n
        rightSum=[0]*n
        net = 0
        answer=[0]*n
        for i in range(0,n):
            leftSum[i]=net
            net = net+nums[i]
        for i in range(0,n):
            net = net-nums[i]
            rightSum[i]=net
        for i in range(0,n):
            answer[i]=abs(leftSum[i]-rightSum[i])
        return answer
            
        
        
        
            
            