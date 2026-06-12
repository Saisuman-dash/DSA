# Implementing hashing using a dictionary
n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]
freq = {}
for i in range(len(n)):
    freq[n[i]] = freq.get(n[i],0)+1
print(freq)
num = int(input("Enter the number in m to find frequency: "))
print(freq.get(num,0))




# # if making it using a list
# hash_list = [0]*10
# for i in range(len(n)):
#     if hash_list[n[i]] == 0:
#         hash_list[n[i]] = 1
#     else:
#         hash_list[n[i]] += 1
# print(hash_list)
# num = int(input("Enter the number in m to find frequency: "))