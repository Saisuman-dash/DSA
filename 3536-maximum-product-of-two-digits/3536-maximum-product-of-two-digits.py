class Solution:
    def maxProduct(self, n: int) -> int:
        nums=[]
        while n!=0:
            nums.append(n%10)
            n=n//10
        nums.sort()
        return nums[-1]*nums[-2]