class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        # def gcd(a:int,b:int):
        #     if b==0:
        #         return a
        #     gcd(b,a%b)
        n=len(nums)
        result=0
        prefixgcd=[1]*n
        sumi=0
        maxi=0
        for i in range (0,n):
            maxi=max(maxi,nums[i])
            result=gcd(nums[i],maxi)
            prefixgcd[i]=result
        prefixgcd.sort()
        left=0
        right=len(prefixgcd)-1
        while left<right:
            pairgcd=gcd(prefixgcd[left],prefixgcd[right])
            sumi=sumi+pairgcd
            left+=1
            right-=1
        return sumi