class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        S = set(nums)
        longest = 0

        for num in S:
            if num - 1 not in S:   
                length = 1

                while num + length in S:
                    length += 1

                longest = max(longest, length)
        return longest