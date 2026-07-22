class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def leftrotate(start,end,arr):
            while start<end:
                arr[start],arr[end]=arr[end],arr[start]
                start+=1
                end-=1
        n=len(nums)
        k=k%n
        if k==0:
            return nums
        leftrotate(n-k,n-1,nums)
        leftrotate(0,n-k-1,nums)
        return leftrotate(0,n-1,nums)
        