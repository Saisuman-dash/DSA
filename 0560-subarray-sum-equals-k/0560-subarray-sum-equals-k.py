class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        freq={0:1}
        sumi=0
        for i in range (len(nums)):
            sumi+=nums[i]
            if sumi-k in freq:
                count+=freq[sumi-k]
            freq[sumi]=freq.get(sumi,0)+1
        return count


