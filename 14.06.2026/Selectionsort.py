# nums = [5,7,8,4,1,6,9,2]
n = int(input("Enter the length of the array :"))
nums =[]
for i in range(n):
    ap=int(input(f"Enter {i}th elements of the array :"))
    nums.append(ap)

for i in range (0,len(nums)):
    min = i
    for j in range (i+1,len(nums)):
        if(nums[j]<nums[min]):
            min = j
    nums[i],nums[min]=nums[min],nums[i]
print(nums)
#Time complexity = O(n^2) as we are using two loops 



# Descending order selection sort 
# Just change the loop condition 
# nums = [5,7,8,4,1,6,9,2]
n = int(input("Enter the length of the array :"))
nums =[]
for i in range(n):
    ap=int(input(f"Enter {i}th elements of the array :"))
    nums.append(ap)

for i in range (0,len(nums)):
    min = i
    for j in range (i+1,len(nums)):
        if(nums[j]>nums[min]):
            min = j
    nums[i],nums[min]=nums[min],nums[i]
print(nums)
        