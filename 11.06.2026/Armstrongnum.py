#Check if a number is an armstrong number or not 
from math import *
n = int(input("Enter a number: "))
po = len(str(n))
num = n
sum =0
while(num>0):
    dig = num%10
    sum = sum + pow(dig,po)
    num =num//10
if sum == n:
    print("number is an Armstrong number")
else:
    print("number is not an Armstrong number")
# time complexity = O(log10n) as we are dividing the number by 10 in each iteration
# space complexity = O(1) as we are only using 3 variables to store the values