class Solution:
    def fib(self, n: int) -> int:
        ans=0
        if n==0 or n==1:
            return n
        ans = self.fib(n-1)+self.fib(n-2)
        return ans
        