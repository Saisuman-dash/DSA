class Solution:
    def minimumPushes(self, word: str) -> int:
        if len(word)<8:
            return len(word)
        count=0
        push=1
        ans=0
        for i in range(0,len(word)):
            if count<8:
                ans+=push
                count+=1
            if count==8:
                push+=1
                count=0
        return ans
            
            
            
        

