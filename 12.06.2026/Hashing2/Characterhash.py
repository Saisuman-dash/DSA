# S = "azyxyyzaaaa"
# q = ["d","a","y","x"]
# freq = {}
# for i in range(len(S)):
#     asci = ord(S[i])
#     freq[asci] = freq.get(asci,0)+1
# print(freq)
# charac = input("Enter the character in q to find frequency: ")
# conv = ord(charac)
# print(freq.get(conv,0))
    



S = "azyxyyzaaaa"
q = ["d","a","y","x"]
hash = [0]*26
for ch in S:
    hash[ord(ch)-ord('a')] += 1
search = input("Enter the character in q to find frequency: ")
print(hash[ord(search)-ord('a')])