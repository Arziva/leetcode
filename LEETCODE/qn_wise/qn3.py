class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        lens = len(s)
        test = ""
        max_count = 0
        if( lens == 0 or lens == 1):
            return lens
        
        for c in s:
            if c in test:
                test = test[test.index(c)+1:]
            test = test + c
            if max_count < len(test):
                max_count = len(test)
        return max_count

        """
        left = 0
        right = 0 
        seen ={}
        answer = 0

        while left < lens and right < lens:
            current = s[right]
        """


        """
        #count = 1
        #max_count = 1
        lens = len(s)
        #st = s[0]
        for i in range(0,lens-1):
            for j in range(s):
                #if (max_count < count):
                #   max_count = count/
                if (j=1 && s[i] != s[j] ):
                    count += 1
                    st = st + s[j]

                

                else:
                    count = 1
        return max_count

        """

