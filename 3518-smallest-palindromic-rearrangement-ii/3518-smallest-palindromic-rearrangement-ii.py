import collections

class Solution:
    def __init__(self):
        self.MAX = 10**6 + 1

    def smallestPalindrome(self, s: str, k: int) -> str:
        count = collections.Counter(s)

        halfCount = [0] * 26
        midLetter = ""

        for c, freq in count.items():
            halfCount[ord(c) - ord("a")] = freq // 2
            if freq % 2:
                midLetter = c

        totalPerm = self.countArrangements(halfCount)

        if k > totalPerm:
            return ""

        halfLen = sum(halfCount)
        left = []

        for _ in range(halfLen):
            for i in range(26):
                if halfCount[i] == 0:
                    continue

                halfCount[i] -= 1
                ways = self.countArrangements(halfCount)

                if ways >= k:
                    left.append(chr(i + ord("a")))
                    break

                k -= ways
                halfCount[i] += 1

        return "".join(left) + midLetter + "".join(reversed(left))

    def countArrangements(self, cnt):
        total = sum(cnt)
        ans = 1

        for f in cnt:
            ans *= self.nCk(total, f)

            if ans >= self.MAX:
                return self.MAX

            total -= f

        return ans

    def nCk(self, n, k):
        ans = 1

        for i in range(1, min(k, n - k) + 1):
            ans = ans * (n - i + 1) // i

            if ans >= self.MAX:
                return self.MAX

        return ans