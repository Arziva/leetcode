class Solution:
    def plusOne(self, digits):
        length = len(digits) - 1
        while digits[length] == 9:
            digits[length] = 0
            length -= 1
        if(length < 0):
            digits = [1] + digits
        else:
            digits[length] += 1
        return digits
"""    
def plusOne(self, digits):
        lens = len(digits) - 1

        for i in range(lens, -1, -1):
            if(i == lens and digits[i] != 9):
                digits[i] += 1
            
            elif(digits[i]>=9 and len(digits)==1):
                ls = [1,0]
                return ls 
            
            elif(digits[i]>=9):
                digits[i] = 0
                digits[i-1] += 1

        return digits
"""