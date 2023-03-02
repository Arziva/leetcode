#recursive caching sol.
#time comp = O(n) and space comp = O(1)
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s) : 1}

        def dfs(i):
            if i in dp:             #if pointer at last position or already been cached
                return dp[i]
            if s[i] == '0':         #if first char is 0
                return 0

            res = dfs(i + 1)         #adding another digit.. dfs[i] = dfs[i+1] + dfs[i+2]
            if (i + 1 < len(s) and (s[i] == "1" or #inbound and starts with one
            s[i] == "2" and s[i+1] in "0123456")):  #ib and starts with 2+0-6
                res += dfs(i+2)                        
            dp[i] = res        #caching the result
            return res
        return dfs(0)

