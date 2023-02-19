from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs):
        #our ord val storing dict
        ord_val = defaultdict(list)
        
        #iterating to find the ord val of the dict
        for i in strs:
            sum = 0
            for j in i:
                sum += ord(j) 
            ord_val[sum].append(i)


        return ord_val.values()


#return error as ord val might store "duh" == "ill" as the ord values are the same