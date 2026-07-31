class Solution:
    def minimumPushes(self, word: str) -> int:
        push=0
        freq={}
        for ch in word:
            freq[ch]=freq.get(ch,0)+1
        freqc=sorted(freq.values(),reverse=True)
        it=0
        for i in range(len(freqc)):
            pushed = (i // 8) + 1
            it+= freqc[i] * pushed

        return it