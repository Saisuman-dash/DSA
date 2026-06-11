#Check whether a number is pallindrome of not 
from math import *
n = int(input("Enter a number: "))
num = n
first = 0
while(num>0):
    mul = num%10
    first = first*10+mul
    num = num//10
if first == n:
    print("number is pallindrome")
else:
    print("number is not a pallindrome")

# time complexity = O(log10n) as we are dividing the num by 10 in each iteration
#space complexity = O(1) as we are only using 2 variables to store the values
