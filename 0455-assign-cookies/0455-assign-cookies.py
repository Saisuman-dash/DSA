class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        n = len(g)
        p= 0
        m=len(s)

        count = 0
        for i in range(0,m):
            if p<n and g[p]<=s[i]:
                count+=1
                p+=1
        return count
            


        