class Solution:
    def trap(self, height: List[int]) -> int:
        
        total=0
        left=0
        right=len(height)-1
        leftmax=float('-inf')
        rightmax=float('-inf')

        while left<right:
            if height[left]<=height[right]:
                leftmax=max(leftmax,height[left])
                total+=leftmax-height[left]
                left+=1
            elif height[left]>height[right]:
                rightmax=max(rightmax,height[right])
                total+=rightmax-height[right]
                right-=1
        return total





        # for i in range (len(height)):
            
        #     total+=min(leftmaxi[i],rightmaxi[i])-height[i]
        
        # return total


            # for i in range (len(leftmaxi)):
        #     if height[i]>leftmax:
        #         leftmax=height[i]
        #     leftmaxi[i]=leftmax
        # print(leftmaxi)
        # for j in range (len(rightmaxi)-1,-1,-1):
        #     if height[j]>rightmax:
        #         rightmax=height[j]
        #     rightmaxi[j]=rightmax
        # print(rightmaxi)

       