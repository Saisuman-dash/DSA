class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        income={5:0,10:0}
        toret=True
        for i in bills:
            if i==5:
                income[i]+=1
            else:
                # if i==5 and income[5]>=1:
                if i==10 and income[5]>=1:
                    income[5]-=1
                    income[i]+=1
                elif i==20 and (income[10]>=1 and income[5]>=1) or (income[5]>=3):
                    if income[10]>=1 and income[5]>=1:
                        income[10]-=1
                        income[5]-=1
                        # income[20]+=1
                    elif income[5]>=3:
                        income[5]-=3
                        # income[20]+=1
                else:
                    return False
        return toret
            

        