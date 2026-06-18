class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        S = set()
        S.update(nums)
        lst = list(S)
        lst.sort()
        n = len(lst)
        maxi = 0
        count = 1
        if (n==1):
            return 1
        for i in range(1,n):
            
            if (lst[i]==lst[i-1]+1):
                count += 1
            else:
                count = 1
            maxi = max(maxi,count)
        
        maxz = int(maxi)
        return int(maxz)