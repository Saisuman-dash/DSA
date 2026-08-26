class Solution(object):
    def shortestBeautifulSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        left=0
        right=0
        ansu=[]
        freq={'0':0,'1':0}
        while right<len(s):
            freq[s[right]]=freq.get(s[right],0)+1
            while freq['1']>k:
                if s[left]=='1':
                    freq['1']-=1
                left+=1
            while freq['1'] == k and s[left] == '0':
                left += 1
            if freq['1']==k:
                st=s[left:right+1]
                print(st)
                ansu.append(st)
            right+=1
        if len(ansu)==0:
            return ""
        return min(ansu, key=lambda x: (len(x), x))
        
        

        
