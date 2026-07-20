class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        
        j = 0  # target pointer
        
        for i in range(1, n+1):
            if j == len(target):
                break
            
            ans.append("Push")
            
            if target[j] == i:
                j += 1
            else:
                ans.append("Pop")
                
        return ans