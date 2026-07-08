class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack=[]
        ans = [-1]*n
        for i in range(n-1,-1,-1):
            stack.append(nums[i])
        for i in range(n-1,-1,-1):
            while len(stack) and stack[-1]<=nums[i]:
                stack.pop()
            if len(stack):
                ans[i]=stack[-1]
            stack.append(nums[i])
        return ans