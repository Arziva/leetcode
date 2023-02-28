class Solution:
    def combinationSum(self, candidates: int, target: int):
        res = []
        #i - index pointer, cur- current list of combination of all values, total value
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy()) #copying so that we can further use this cur
                return
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res