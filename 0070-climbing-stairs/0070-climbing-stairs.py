class Solution:
    def climbStairs(self, n: int) -> int:
        hash={}
        ans=0
        def climb(n):
            if n==1 or n==2:
                return n
            if n in hash:
                return hash[n]
            else:
                ans = climb(n-1)+climb(n-2)
                hash[n]=ans
                return ans
        return climb(n)