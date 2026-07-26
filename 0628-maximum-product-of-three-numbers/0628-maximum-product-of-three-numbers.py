class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n=len(nums)
        productmax=nums[0]*nums[1]*nums[2]
        productmin=nums[n-1]*nums[n-2]*nums[0]
        return max(productmax,productmin)