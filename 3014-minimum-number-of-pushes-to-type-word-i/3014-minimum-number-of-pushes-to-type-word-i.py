class Solution:
    def minimumPushes(self, word: str) -> int:
        w=len(word)//8
        e=len(word)%8
        filled= (w*(w+1))//2
        filled=8*filled
        extra= e*(w+1)
        ans=filled+extra
        return ans
            
            
            
        

