class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        maxalt=0
        act =0
        for i in range(0,n):
            act = act + gain[i]
            maxalt = max(maxalt,act)
        return maxalt
        