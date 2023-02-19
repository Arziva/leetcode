from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        #our val storing dict
        result = defaultdict(list)
        
        #iterating to find the val of the strs
        for i in strs:
            count = [0] * 26

            #find the count val of each str
            for c in i:
                count[ord(c) - ord("a")] += 1
            
            
            result[tuple(count)].append(i) #changed to list to tuple as list cannot be keys

        return result.values()
