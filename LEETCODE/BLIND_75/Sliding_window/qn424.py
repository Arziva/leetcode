class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} #occurance of each char
        res = 0 #store longest val

        l = 0 
        for r in range(len(s)): #iterating through the right pointer
            count[s[r]] = 1 + count.get(s[r], 0) #incrementing the right pointer by one
            # one plus what the count was, or change it to zero

            if(r - l + 1) - max(count.values()) > k:    #checking if sliding - max is greater than the value of k(variables we can change)
                count[s[l]] -= 1        #remove the left val
                l += 1                  #increase the left pointer to shorten the sliding window

            res = max(res, r - l + 1)   
        
        return res
        