class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count={}
        n=len(fruits)
        left=0
        right=0
        maxi =0
        while right<n:
            count[fruits[right]]=count.get(fruits[right],0)+1
            while len(count)>2:
                count[fruits[left]]-=1
                if count[fruits[left]]==0:
                    del count[fruits[left]]
                left += 1
            maxi = max(maxi,right-left+1)
            right += 1
        return maxi

            