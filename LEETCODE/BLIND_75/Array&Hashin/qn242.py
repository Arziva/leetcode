class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = []
        for i in s:
            arr.append(i)
        for i in t:
            if i in arr:
                arr.remove(i)
            else:
                return False
        return len(arr) == 0