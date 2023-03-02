class Solution:
    def countSubstrings(self, s: str) -> int:

        def check_pal(x):
            l, r = 0, len(x)-1
            while l < r:
                if x[l] != x[r]:
                    return False
                l += 1
                r -= 1
            return True

        res = []

        for i in range(len(s)):
            str1 = s[i]
            if(check_pal(str1) == True):
                res.append(str1)
            for j in range(i+1, len(s)):
                str1 += s[j]
                if(check_pal(str1) == True):
                    res.append(str1)
        print(res)
        return len(res)