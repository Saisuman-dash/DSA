# arr = [1,2,3,4,5,6,7]
# n = len(arr)-1
# i=0
# revarr = []

# def rev(revarr,arr,i,n):
#     if i>n :
#         print(revarr)
#         return
#     a=n-i
#     revarr.append(arr[a])
#     rev(revarr,arr,i+1,n)

# rev(revarr,arr,i,n)













arr = [1,2,3,4,5,6,7]
arrc = arr.copy()
left = int(input("Enter the left index:"))
right = int(input("Enter the right index:"))
if left<0 or right>=len(arr):
    print("Invalid input")
    exit()
print(f"The original array was {arr}")
def rev(arrc,l,r):
    if l>=r:
        print(f"the reversed array from index {left} to {right} is {arrc}")
        return
    arrc[l],arrc[r] = arrc[r],arrc[l]
    l +=1
    r -=1
    rev(arrc,l,r)

rev(arrc,left,right)