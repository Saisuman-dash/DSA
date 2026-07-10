class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        sum = 0
        maxi = 0
        left = 0
        right = n-1
        if k == n:
            for i in range (0,n):
                sum = sum+cardPoints[i]
            return sum
        
        while left<k:
            sum = sum + cardPoints[left]
            left+=1
            maxi = max(maxi,sum)
        left -=1
        for i in range (0,k):
            sum = sum-cardPoints[left]+cardPoints[right]
            maxi = max(maxi,sum)
            left -= 1
            right -= 1
        return maxi
        
        


        