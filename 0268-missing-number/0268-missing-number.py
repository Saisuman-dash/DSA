class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        net=n*(n+1)//2
        sumnet=sum(nums)
        if sumnet==net:
            return 0
        return net-sumnet