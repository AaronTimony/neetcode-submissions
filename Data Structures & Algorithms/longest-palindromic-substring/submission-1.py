class Solution:
    def longestPalindrome(self, s: str) -> str:
        i = 0
        res = 0
        resLen = 0
        n = len(s)

        while i < n:
            # odd case
            l = i
            r = i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                
                if r - l + 1 > resLen:
                    res = l
                    resLen = r - l + 1

                l -= 1
                r += 1

            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > resLen:
                    res = l
                    resLen = r - l + 1

                l -= 1
                r += 1

            i += 1

        return s[res: res + resLen]