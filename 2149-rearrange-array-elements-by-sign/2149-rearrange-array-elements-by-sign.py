class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        final =[0]*n
        p = 0
        ne = 1

        for i in range(0,n):
            if (nums[i]>0):
                final[p]=nums[i]
                p+=2
            else:
                final[ne]=nums[i]
                ne+=2
        return final   