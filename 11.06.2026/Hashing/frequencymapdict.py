# Creating a frequency map usign a dictionary
num = [5,6,7,7,1,9,111,1,1,5,1,1]
n = int(input("Enter a number to find its frequency:"))
freq = {}
for i in range(0,len(num)):
    if num[i] in freq:
        freq[num[i]] += 1
    else:
        freq[num[i]]=1
print(freq)
if n not in freq:
    print("Number does not exist in list")
else:
    print(f"The frequency of {n} is {freq[n]}")
# all the operation in dictionary takes O(1) time complexity so we are only bothered about the loop and that is of O(n) time complexity


#BEST APPROACH : Using the .get method of dictionary to avoid the if else condition
num = [5,6,7,7,1,9,111,1,1,5,1,1]
n = int(input("Enter a number to find its frequency:"))
freq = {}
for i in range(0,len(num)):
    freq[num[i]] = freq.get(num[i],0) + 1 # this will return the value of num[i] if it exists in the dictionary and if it does not exist then it will return 0 and then we are adding 1 to it
print(freq)
if n not in freq:
    print("Number does not exist in list")
else:
    print(f"The frequency of {n} is {freq[n]}")
