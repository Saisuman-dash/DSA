# nums = [5,7,8,4,1,6,9,2]
n = int(input("Enter the length of the array :"))
nums =[]
for i in range(n):
    ap=int(input(f"Enter {i}th elements of the array :"))
    nums.append(ap)
for i in range(0,len(nums)):
    for j in range (0,len(nums)-i-1):
        swapped = False
        if (nums[j]>nums[j+1]):
            nums[j+1],nums[j]=nums[j],nums[j+1]
            swapped = True
    if not swapped :
        break
print(nums)
#Time complexity O(n^2) in avg and worst case but O(n) in best case if array is sorted as we are using the swapped flag

