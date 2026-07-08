class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        self.nums=asteroids
        self.n=len(self.nums)
        self.stack=[]
        
        for i in range(0,self.n):
            self.zinda = True
            while len(self.stack) and self.nums[i]<0 and self.stack[-1]>0:
                if abs(self.nums[i])>self.stack[-1]:
                    self.stack.pop()
                elif abs(self.nums[i])<self.stack[-1]:
                    self.zinda = False
                    break
                elif abs(self.nums[i])==self.stack[-1]:
                    self.stack.pop()
                    self.zinda = False
                    break
            if self.zinda:
                self.stack.append(self.nums[i])
            
        return self.stack
        