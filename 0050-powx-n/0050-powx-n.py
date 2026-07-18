class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans=1
        if n<0:
            x=1/x
            n=-n
        if n==0:
            return 1
        if n==1:
            return x
        if n % 2==0:
            ans=self.myPow(x,n//2) 
            return ans*ans
        else:
            ans=self.myPow(x,n//2)
            return ans*ans*x
        