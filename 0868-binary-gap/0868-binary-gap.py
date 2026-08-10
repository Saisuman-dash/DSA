class Solution:
    def binaryGap(self, n: int) -> int:
        a=bin(n)[2:]
        maxi=float('-inf')
        j=0
        i=0
        while j<len(a):
            if a[j]=='1':
                dist=j-i
                i=j
                maxi=max(maxi,dist)
            j+=1
        return maxi
        