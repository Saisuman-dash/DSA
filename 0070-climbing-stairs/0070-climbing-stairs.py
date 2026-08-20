class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        def ppt(n,qb):
            if n<0:
                return 0
            if n==0:
                return 1
            if n in qb:
                return qb[n]
            bugu=ppt(n-1,qb)+ppt(n-2,qb)
            qb[n]=bugu
            return bugu
        qb={}
        ansu=ppt(n,qb)
        return ansu
        