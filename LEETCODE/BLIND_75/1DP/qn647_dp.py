class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        #palindrome counter using pointers expansion
        def count_pal(s, l, r):
            res = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            return res

        for i in range(len(s)):
            res += count_pal(s, i, i) #for checking palindromes of odd length
            res += count_pal(s, i, i+1) #for checking pals of even length

        return res