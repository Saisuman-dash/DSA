#find the factors of a number and print them out
num= int(input("Enter a number: "))
print("The factors of", num, "are:")
out =[1,num]
for i in range(2,(num//2)+1):
    if num%i == 0:
        out.append(i)
out.sort()
print(out)
# time complexity = O(n/2) as we are iterating through all the numbers from 2 to n/2
# space complexity = O(n) as we are storing the factors in a list which can grow


#BEST APPROACH : Go till the root of the number and find both the factors at the same time 
#find the factors of a number and print them out
from math import *
num= int(input("Enter a number: "))
print("The factors of", num, "are:")
out =[1,num]
for i in range(2,int(sqrt(num)+1)):
    if num%i == 0:
        out.append(i)
        if num//i != i:
            out.append(num//i)
        
out.sort()
print(out)
# time complexity = O(root(n)) as we are iterating through all the numbers from 2 to root(n) + O(log(n)) for sorting the factors
# space complexity = O(n) as we are storing the factors in a list which can grow