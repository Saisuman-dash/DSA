class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        maxi=0
        area=0
        right=n-1
        left=0
        while left<right:
            area=(right-left)*min(height[right],height[left])
            maxi=max(maxi,area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxi
