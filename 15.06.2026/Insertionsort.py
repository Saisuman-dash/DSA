
n = int(input("Enter the length of the array :"))
nums =[]
for i in range(n):
    ap=int(input(f"Enter {i}th elements of the array :"))
    nums.append(ap)
for i in range(1,len(nums)):
    key = nums[i]
    j = i-1
    while j>=0 and nums[j]>key:
        nums[j+1] = nums[j]
        j -= 1
    nums[j+1] = key
print(f"After insertion sort the sorted array is : {nums}")

# Time complexity 
# Best case: O(n) - when the array is already sorted
# Average case: O(n^2) - when the array is randomly ordered
# Worst case: O(n^2) - when the array is sorted in reverse order

#Space complexity O(1) 
# as we are not using any extra space for sorting the array 
# we are just using a key variable to store the current element and j variable to store the index of the previous element.