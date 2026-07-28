class Solution:
    def longestPalindrome(self, s: str) -> str:
        leng = 1
        orbit = 1
        ans = s[0]

        if len(s) == 1:
            return s


        for axis in range(len(s)):
            leng = 1
            orbit = 1

            while (axis - orbit) >= 0 and (axis + orbit) < len(s):
                if s[axis - orbit] == s[axis + orbit]:
                    orbit += 1
                    leng += 2

                    if leng > len(ans):
                        ans = s[axis - orbit + 1 : axis + orbit]
                else:
                    break

     
        for axis in range(len(s) - 1):
            leng = 0
            orbit = 1

            while (axis - orbit + 1) >= 0 and (axis + orbit) < len(s):
                if s[axis - orbit + 1] == s[axis + orbit]:
                    orbit += 1
                    leng += 2

                    if leng > len(ans):
                        ans = s[axis - orbit + 2 : axis + orbit]
                else:
                    break

        return ans