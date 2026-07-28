class Solution:
    def trap(self, height: List[int]) -> int:
        
        total=0
        leftmaxi=[0]*len(height)
        rightmaxi=[0]*len(height)
        leftmax=float('-inf')
        rightmax=float('-inf')

        for i in range (len(leftmaxi)):
            if height[i]>leftmax:
                leftmax=height[i]
            leftmaxi[i]=leftmax
        for j in range (len(rightmaxi)-1,-1,-1):
            if height[j]>rightmax:
                rightmax=height[j]
            rightmaxi[j]=rightmax
        for i in range (len(height)):
            total+=min(leftmaxi[i],rightmaxi[i])-height[i]
        
        return total
       