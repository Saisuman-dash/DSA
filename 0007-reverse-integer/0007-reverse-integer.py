class Solution:
    def reverse(self, x: int) -> int:
        p=abs(x)
        tenp=1
        ans=0
        val=0
        while p//1!=0:
            val=p%10
            ans=ans*10+val
            tenp*=10
            p=p//10
        if x<0:
            ans= -1*ans
        if ans<=(-1*2**31) or ans>=(2**31)-1:
            return 0
        return ans
