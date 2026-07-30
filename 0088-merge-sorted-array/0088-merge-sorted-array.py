class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # if m==0:
        #     nums1=nums2
        ans=[]
        p=0
        i=0
        j=0
        while i<=m-1 and j<=n-1:
            if nums1[i]<=nums2[j]:
                ans.append(nums1[i])
                i+=1
               
            else:
                ans.append(nums2[j])
                j+=1
        while i < m:
            ans.append(nums1[i])
            i += 1
        while j < n:
            ans.append(nums2[j])
            j += 1
        for i in range (len(ans)):
            nums1[i]=ans[i]