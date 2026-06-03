class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False

                l += 1
                r -= 1

            return True

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1

            else:
                if is_palindrome(l + 1, r) or is_palindrome(l, r - 1):
                    return True

                else:
                    return False

        return True