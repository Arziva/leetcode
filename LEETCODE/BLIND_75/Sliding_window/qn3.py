class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxcount = 0
        temp = ""
        for c in s:
            if c in temp:
                temp = temp[temp.index(c)+1:]
            temp += c
            if len(temp) > maxcount:
                maxcount = len(temp)

        return maxcount
