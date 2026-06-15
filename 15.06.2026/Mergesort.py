  
def mergetsa(left,right):
    res = []
    i,j = 0,0
    n = len(left)
    m = len(right)
    while i<n and j<m:
        if(left[i]<right[j]):
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    while i<n:
        res.append(left[i])
        i+=1
    while j<m:
        res.append(right[j])
        j+=1
    return res
def mergesort(nums):

    if len(nums)<=1:
        return nums
    mid = len(nums)//2
    left_arr = nums[:mid]
    right_arr = nums[mid:]
    left = mergesort(left_arr)
    right = mergesort(right_arr)
    store = mergetsa(left,right)
    return store

def main():
    n = int(input("Enter the length of the array :"))
    nums =[]
    for i in range(n):
        ap=int(input(f"Enter {i}th elements of the array :"))
        nums.append(ap)
    rest = mergesort(nums)
    print(f"After merge sort the sorted array is : {rest}")
if __name__ == "__main__":
        main() 

