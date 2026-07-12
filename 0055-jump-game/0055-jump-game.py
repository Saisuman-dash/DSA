class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        reached=0
        jump=0
        i=0
        if n == 1:
            return True
        while i<n:
            if i > reached:
                return False
            reached=max(reached,i+nums[i])
            if reached>=n-1:
                return True
            i+=1
        return False
        