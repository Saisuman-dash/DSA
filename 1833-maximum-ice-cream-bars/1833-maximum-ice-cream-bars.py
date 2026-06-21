class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        sumi = 0
        count = 0
        n=len(costs)
        for i in range(0,n):
            sumi = sumi + costs[i]
            if (sumi<=coins):
                count+=1
            else:
                break
        return count
# 2.3.3.5.6.6.6.7.9.10
# 0.2.5.8.13.19.25.31.38.47.
# 0.1.2.3.4.5.6.7.8.9.          